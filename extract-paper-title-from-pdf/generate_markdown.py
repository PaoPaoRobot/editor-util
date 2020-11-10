import os
import os
import re
import string
import sys

from PyPDF2 import PdfFileWriter, PdfFileReader



filePath = '/home/song/Desktop/iros2020/'
file_list = os.listdir(filePath)

file_list.sort()
file_f = open("txt.md", "w+")

data_url_prefix = 'https://ras.papercept.net/proceedings/IROS20/'

file_f.write("| index | title |\n")
file_f.write("|---|---|\n")



for name in file_list:
    filename = filePath + name
    name_prefix = name.split(".")[0]
    try:
        pdf_reader = PdfFileReader(open(filename, 'rb'))     
        paper_title = pdf_reader.getDocumentInfo().title       
        print(paper_title)
        file_f.write("| [{}]({}) | {} |\n".format(name_prefix, data_url_prefix+name , paper_title))
    except Exception:
        continue
