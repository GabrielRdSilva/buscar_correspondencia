# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:22:29 2023

@author: gabriel.rodrigues
"""
import fitz

def search_text_in_pdf(file_path, text_to_search):
    results = []
    doc = fitz.open(file_path)

    for page_num, page in enumerate(doc):
        text = page.get_text('text')
        for text_to_search in text:
            results.append((page_num + 1, text))

    return results
pdf_file = R'C:\Users\gabriel.rodrigues\Desktop\teste 2\exclsuive\bloco 1\apartamento 1\cota 1\ok2.pdf'  # Replace with the path to your PDF file
search_text = "JOAO"  # Replace with the text you are searching for

search_results = search_text_in_pdf(pdf_file, search_text)

if search_results:
    print(f"Text found in {len(search_results)} page(s):")
    for page_num, text in search_results:
        print(f"  - Page {page_num + 1}: {text}")
else:
    print("Text not found.")