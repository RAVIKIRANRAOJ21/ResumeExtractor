import spacy
import docx2txt
nlp = spacy.load('en')
cool=docx2txt.process("Nikhilresume.docx")
docx1 = nlp(cool)
def damn(text):
    docx = nlp(text)
    redacted_sentences = []
    for ent in docx.ents:
        ent.merge()
    for token in docx:
        if token.ent_type_ == 'PERSON':
            print(token)       
        else:
            redacted_sentences.append(token.string)
    return "".join(redacted_sentences) 
damn(cool)