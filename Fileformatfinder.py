import fnmatch                        #fnmatch function is used to match the string 
import os

def fileformat(path):
    for file in os.listdir(path):         #path = current directory path
        if fnmatch.fnmatch(file, '*.docx'):
            return docx
        elif fnmatch.fnmatch(file, '*.pdf'):
            return PyPDF2
        elif fnmatch.fnmatch(file, '*.rtf'):
            return rtf
        elif fnmatch.fnmatch(file, '*.zip'):
            return zip
