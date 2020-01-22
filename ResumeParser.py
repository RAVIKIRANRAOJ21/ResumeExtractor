import string
import re
import spacy
import pandas as panda
import os
from doc2txt import doc2txt
from pdf2txt import pdf2txt

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
    name  = str(filtered[0])+' ' +str(filtered[1])        # logic is wrong, need to be improved.
    return name

def skills(path):
    nlp = spacy.load('en_core_web_sm')
    my_text = nlp(doc2txt(path))
    # my_text = nlp(pdf2txt(path))
    nounchunks = list(my_text.noun_chunks)
    tokens = [token.text for token in my_text if not token.is_stop]
    data = panda.read_csv(os.path.join(os.path.dirname(__file__), 'technical_skills.csv'))
    skills = list(data.columns.values)
    skill_set = []
    for token in tokens:
        if token.lower() in skills:
            skill_set.append(token)
    for token in nounchunks:
        token = token.text.lower().strip()
        if token in skills:
            skill_set.append(token)
    return [i.capitalize() for i in set([i.lower() for i in skill_set])]

Path = 'C://Users//kiran//Desktop//resume.docx'

print("Name : " + Name(Path))
print("Email : " + email(Path))
print("Phone Numbers : " + PhoneNo(Path))
print("Experience : " + experience(Path))
print("Skills : " + str(skills(Path)))
