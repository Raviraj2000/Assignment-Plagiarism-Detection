import streamlit as st
from process import get_tensors, get_similar
import pandas as pd

def check_similarity(files):
    with st.spinner('Calculating embeddings....'):
        tensors = get_tensors(files)
        
    with st.spinner("Check Similarity...."):
        ans = get_similar(tensors)
     
    df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in ans.items() ]))
    
    #df = pd.DataFrame.from_dict(ans)
    
    st.subheader("Plagiarized Assignments")
    
    st.dataframe(df.T)
    
    return

files = st.file_uploader("Upload files", key='files', type=['zip'])

check = st.button("Check Similarity", key='checksimilarity')

if check:
    if files == None:
        st.error("Please Upload Files in Zip Format")
    else:     
        check_similarity(files)