from PyPDF2 import PdfFileReader
import PyPDF2



path=r'D:\\Projects\\Python\\PDF\\1.pdf'
pdf_reader=PyPDF2.PdfFileReader(open(path,"rb"))

print(pdf_reader.getNumPages())
