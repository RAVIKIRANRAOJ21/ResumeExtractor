import PyPDF2

fl = open('C://Users//kiran//Desktop//resume.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(fl)

nop = pdfReader.numPages

for i in range(nop):
     pageObj = pdfReader.getPage(i)
     print(pageObj.extractText())

fl.close()
