import pdfplumber
import re


def extract_theory(file_name):
    
    ext_text = []
    
    with pdfplumber.open(file_name) as pdf:
        page = pdf.pages
        for i in page:
            ext_text.append(i.extract_text(x_tolerance=3, y_tolerance=3, layout=False, x_density=7.25, y_density=13))
            
    ext_text = ' '.join(ext_text)
    
    keyword = 'Theory:'
    before, keyword, text = ext_text.partition(keyword)
    
    return text