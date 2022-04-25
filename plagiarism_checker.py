from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('stsb-mpnet-base-v2')

def get_similarity(text1, text2):
    
    embedding1 = model.encode(text1, convert_to_tensor=True)
    embedding2 = model.encode(text2, convert_to_tensor=True)
    
    cosine_scores = util.cos_sim(embedding1, embedding2)
    
    return cosine_scores.item()
