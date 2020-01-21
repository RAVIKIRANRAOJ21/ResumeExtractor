from doc2txt import doc2txt
from pdf2txt import pdf2txt

import re
import string

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

def experience(path):
    my_text = doc2txt(path)
#     my_text= pdf2txt(path)
    pattern=re.compile(r"(\d+(?:-\d+)?\+?)\s*(years?)", re.I)
    matches=pattern.finditer(my_text)
    for x in matches:
        return x.group()

def Name(path):
    my_text=pdf2txt(path)
    # my_text=doc2txt(path)
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    #resume = getText(Nikhilresume).encode("ascii", "ignore")
    #print ("tokenizing the given file ......")
    tokens = word_tokenize(my_text)
    punctuations = ['(',')',';',':','[',']',',']
    stop_words = stopwords.words('english')
    #storing the cleaned resume
    filtered = [w for w in tokens if not w in stop_words and  not w in string.punctuation]
    #print ("removing the stop words....\nCleaning the resumes....\nExtracting Text .......")
    #print (filtered)
    #get the name from the resume
    name  = str(filtered[0])+' ' +str(filtered[1])
    print ("Name : "+ name)

# print(Name('C://Users//kiran//Desktop//resume.pdf'))    

# print("Experience : " + experience('C://Users//kiran//Desktop//Resume3.pdf'))

# print("Phone Numbers : " + PhoneNo('C://Users//kiran//Desktop//resume.pdf'))

# print("Email : " + email('C://Users//kiran//Desktop//resume.docx'))
