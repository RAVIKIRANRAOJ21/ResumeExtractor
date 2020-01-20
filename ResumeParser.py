from doc2txt import doc2txt
from pdf2txt import pdf2txt

import re


def email(path):
    tmp = doc2txt(path)
#     tmp = pdf2txt(path)
    pattern=re.compile(r'[a-zA-Z0-9-\.]+@+[a-zA-Z0-9-\.]*')
    matches=pattern.finditer(tmp)
    for i in matches:
        j=i.group(0)
    return j

print(email('C://Users//kiran//Desktop//resume.docx'))
