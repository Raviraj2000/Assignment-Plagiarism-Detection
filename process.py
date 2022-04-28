from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('stsb-mpnet-base-v2')
from extract_text import extract_theory
import zipfile
from io import BytesIO             
import os
from text_preprocess import preprocess


def get_tensors(files):
    extract_dict = dict()
    with zipfile.ZipFile(files,'r') as z: 
        filenames = z.namelist()
        for f in filenames:
            name = os.path.basename(f)
            to_encode = preprocess(extract_theory(BytesIO(z.read(f))))
            extract_dict[name] = model.encode(to_encode, convert_to_tensor=True)
        
    return extract_dict

def get_similar(extract_dict):
    texts = list(extract_dict.items())
    ans = dict()
    check = []
    for i,n in enumerate(texts):
        print(i)
        if i != texts[-1].index:
            answers = []
            for k in range(i+1, len(texts)):
                if texts[k][0] in check:
                    continue
                else:
                    sim = util.cos_sim(n[1], texts[k][1])
                    if sim.item() > 0.75:
                        answers.append((texts[k][0]))
                        check.append(texts[k][0])
                        print("printing check", check)
                    ans[texts[i][0]] = answers
        else:
            break
    
    ans = {k: v for k, v in ans.items() if v}
    print("THIS IS ANS", ans)
    return ans