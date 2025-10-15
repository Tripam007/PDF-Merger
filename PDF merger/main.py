from PyPDF2 import PdfMerger #pdfmerger class is imported from PyPDF2 library

pdfiles = ["1.pdf", "2.pdf"] #name the pdf files u want to merge along with each other
merger = PdfMerger() #merges the pdf files

for filename in pdfiles:
    with open(filename, 'rb') as pdfFile:
        merger.append(pdfFile) 

merger.write("merged.pdf")# the merged pdf is created in the name of "merged.pdf"
merger.close()
