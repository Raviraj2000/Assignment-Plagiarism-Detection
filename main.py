import streamlit as st
from extract_text import extract_theory
from text_preprocess import preprocess
from plagiarism_checker import get_similarity
import time

def check_similarity(file_1, file_2):
    theory_1 = extract_theory(file_1)
    ptext_1 = preprocess(theory_1)

    theory_2 = extract_theory(file_2)
    ptext_2 = preprocess(theory_2)

    with st.spinner('Calculating....'):
        similarity_index = get_similarity(ptext_1, ptext_2)

    st.write(similarity_index)

    if similarity_index > 0.75:
        st.subheader("Document Plagiarized")
    else:
        st.subheader("Document Not Plagiarized")

file_1 = st.file_uploader("Upload first document: ", key='file_1', type=['pdf'])

file_2 = st.file_uploader("Upload second document: ", key='file_2', type=['pdf'])

check = st.button("Check Similarity", key='checksimilarity')

if check:
    if file_1 == None:
        st.error("File 1 missing")
    if file_2 == None:
        st.error("File 2 missing")
    else:     
        check_similarity(file_1, file_2)


