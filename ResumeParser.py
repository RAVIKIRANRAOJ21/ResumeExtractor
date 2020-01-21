from doc2txt import doc2txt
from pdf2txt import pdf2txt

import re


def email(path):
    tmp = doc2txt(path)
#     tmp = pdf2txt(path)
    pattern=re.compile(r'[a-zA-Z0-9-\.]+@+[a-zA-Z0-9-\.]*')
    matches=pattern.findall(tmp)
    mail = ''
    for i in matches:
        mail = mail + '\n' + i
    return mail

def PhoneNo(path):
    tmp = doc2txt(path)
#     tmp = pdf2txt(path)
    pattern = re.compile(r'(\d\d\d\d\d\d\d\d\d\d)')  #  re (phoneno.) logic needs to be improved
    matches = pattern.findall(tmp)
    Number = ''
    for x in matches:
        Number = Number + '\n' + x
    return Number

print(" Phone Numbers : " + PhoneNo('C://Users//kiran//Desktop//resume.pdf'))

print('Email : ' + email('C://Users//kiran//Desktop//resume.docx'))
