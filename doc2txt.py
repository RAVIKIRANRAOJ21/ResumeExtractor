import  docx

def doc2txt(path):
    doc = docx.Document(path)
    completedText = []
    for pg in doc.paragraphs:
        completedText.append(pg.text)
    return '\n' .join(completedText)

print (doc2txt('C://Users//kiran//Desktop//resume.docx'))
