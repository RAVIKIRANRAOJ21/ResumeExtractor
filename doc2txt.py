import  docx

def rtd(fl):
    doc = docx.Document(fl)
    completedText = []
    for pg in doc.paragraphs:
        completedText.append(pg.text)
    return '\n' .join(completedText)

print (rtd('C://Users//kiran//Desktop//resume.docx'))
