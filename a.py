import os

f = open('a.docx',"wb")
f.seek(2147483648-1)
f.write("\0")
f.close()
