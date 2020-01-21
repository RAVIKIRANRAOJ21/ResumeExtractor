from doc2txt import doc2txt
from pdf2txt import pdf2txt
import string
import re

def PhoneNo(path):
    tmp = doc2txt(path)
    # tmp = pdf2txt(path)
    pattern = re.compile(r'(\d\d\d\d\d\d\d\d\d\d)')  # re logic needs to be improved
    matches = pattern.findall(tmp)
    Number = ''
    for x in matches:
        Number = Number + '\n' + x
    return Number

def email(path):
    tmp = doc2txt(path)
    # tmp = pdf2txt(path)
    pattern=re.compile(r'[a-zA-Z0-9-\.]+@+[a-zA-Z0-9-\.]*')
    matches=pattern.findall(tmp)
    mail = ''
    for i in matches:
        mail = mail + '\n' + i
    return mail

def experience(path):
    my_text = doc2txt(path)
    # my_text= pdf2txt(path)
    pattern=re.compile(r"(\d+(?:-\d+)?\+?)\s*(years?)", re.I)
    y = 'None'
    matches=pattern.finditer(my_text)
    for x in matches:
        y = x.group()
    return y

def Name(path):
    my_text=doc2txt(path)
    # my_text=pdf2txt(path)
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
    return name

Path = 'C://Users//kiran//Desktop//resume.docx'

print("Name : " + Name(Path))
print("Email : " + email(Path))
print("Phone Numbers : " + PhoneNo(Path))
print("Experience : " + experience(Path))
