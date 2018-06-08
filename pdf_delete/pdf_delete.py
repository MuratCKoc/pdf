#A short script to delete / remove pages from pdf files
#Author: Koclabs

from PyPDF2 import PdfFileWriter, PdfFileReader

sourcefile = input('Enter a pdf Filename (dont write .pdf): ')
infile = PdfFileReader(sourcefile+".pdf", 'rb')
outfile = input('Enter a Output Filename (dont write .pdf): ')+".pdf"
output = PdfFileWriter()
pageNum = infile.getNumPages


deleteStr = input('Enter pages to delete by comma, Ex 1,4,5: ')
pages_to_delete = [int(x) for x in deleteStr.split(',') if x.strip().isdigit()]
print(pages_to_delete)
#Sort the requested pages to delete
pages_to_delete.sort()
print("Sorted page numbers requested to delete : ",pages_to_delete)

print(range(infile.getNumPages()))

for i in range(infile.getNumPages()):
    if i in pages_to_delete:
        print("Delete page: ", i)
    #avoid adding the last page to first by i!=0
    elif i not in pages_to_delete and i!=0:
        p = infile.getPage(i-1)
        output.addPage(p)

with open(outfile, 'wb') as f:
    output.write(f)
