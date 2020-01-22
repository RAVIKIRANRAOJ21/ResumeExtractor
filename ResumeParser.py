import re
import spacy
import pandas as panda
import os
from doc2txt import doc2txt
from pdf2txt import pdf2txt
from spacy.matcher import Matcher

def PhoneNo(path):
    tmp = doc2txt(path)
    # text = pdf2txt(path)
    pattern = re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{5})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?')
    match = pattern.findall(text)
    if match:
        number = ''.join(match[0])
        if len(number) > 10:
            return '+' + number
        else:
            return number

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
    matches=pattern.finditer(my_text)
    for x in matches:
        return x.group()

def Name(path):
     nlp = spacy.load('en_core_web_sm')
    my_text = nlp(doc2txt(path))
    # my_text = nlp(pdf2txt(path))
    NAME_PATTERN = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    match = Matcher(nlp.vocab)
    pattern = [NAME_PATTERN]
    match.add('NAME', None, *pattern)
    matches = match(my_text)
    for match_id, start, end in matches:
        span = my_text[start:end]
        return span.text

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

def DOB(path):
    my_text = doc2txt(path)
    # my_text = pdf2txt(path)
    pattern = re.compile(r'([0-3]?[0-9](?:\.|\/|\-|\s)[0-3]?(?:[0-9]|' + r'(?:Feb|Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January' + r'|February|March|April|May|June|July|August|September|October|' +r'November|December))(?:\.|\/|\-|\s)(?:[0-9]{2})?[0-9]{2})',re.IGNORECASE | re.UNICODE)
    matches=pattern.finditer(my_text)
    for x in matches:
         return x.group()

Path = 'C://Users//kiran//Desktop//resume.docx'

print("Name : " + str(Name(Path)))
print("Email : " + email(Path))
print("Phone Numbers : " + PhoneNo(Path))
print("Experience : " + experience(Path))
print("Skills : " + str(skills(Path)))
print("Date of Birth : " + DOB(Path))
