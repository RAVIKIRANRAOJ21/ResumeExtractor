import docx2txt
import re
my_text=docx2txt.process("Nikhilresume.docx")
pattern=re.compile(r"(\d+(?:-\d+)?\+?)\s*(years?)", re.I)
#patternn=re.findall(r"([\d+-]+)\s+(years?)", x, re.IGNORECASE)
matches=pattern.finditer(my_text)
for x in matches:
    print(x)
#experience

import docx2txt
import re

my_text=docx2txt.process("Nikhilresume.docx")
pattern=re.compile(r'[a-zA-Z0-9-\.]+@[a-zA-Z-\.]*\.(com|edu|net)')
matches=pattern.finditer(my_text)
for x in matches:
    print(x.group(0))
#mail
