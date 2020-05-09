import sys
import PyPDF2

watermark_needed = sys.argv[1]
pdf_inputs = sys.argv[2:]


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('merged_output.pdf')


pdf_merger(pdf_inputs)

if watermark_needed.lower() == 'y':
    template = PyPDF2.PdfFileReader(open('merged_output.pdf', 'rb'))
    watermark = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
    output = PyPDF2.PdfFileWriter()
    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)
        with open('watermark_output.pdf', 'wb') as file:
            output.write(file)
