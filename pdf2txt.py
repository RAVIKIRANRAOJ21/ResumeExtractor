import PyPDF2

def pdf2txt(path):
    fl = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(fl)
    nop = pdfReader.getNumPages()
    extractedtxt =""
    for i in range(nop):
        pageObj = pdfReader.getPage(i)
        extractedtxt += pageObj.extractText()
    return extractedtxt
    fl.close()

# print (pdf2txt('C://Users//kiran//Desktop//resume.pdf'))
