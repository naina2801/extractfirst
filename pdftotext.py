

# import PyPDF2
#
# pdfFileObj = open(r'C:\Users\Unaina\PycharmProjects\pandas1\assesment\imgpdf.pdf')
#
#
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
# print(pdfReader.numPages)
#
# pageObj = pdfReader.getPage(0)
#
# print(pageObj.extractText())
#
# pdfFileObj.close()

# importing required modules
# import PyPDF2
#
# # create a pdf file object
# # pdfFileObj = open(r'C:\Users\Unaina\PycharmProjects\pandas1\assesment\imgpdf.pdf')
#
# # create a pdf reader object
# pdfReader = PyPDF2.open(r'C:\Users\Unaina\PycharmProjects\pandas1\assesment\imgpdf.pdf')
#
# # print number of pages in the pdf file
# print("Page Number:", pdfReader.numPages)
#
# # create a page object
# pageObj = pdfReader.getPage(1)
#
# # extract text from page
# text = pageObj.extractText()
#
# # display just the text
# print(text)
# import pdf2image
# import pytesseract
# from pytesseract import Output, TesseractError
#
# pdf_path = r'C:\Users\Unaina\PycharmProjects\pandas1\assesment\imgpdf.pdf'
#
# images = pdf2image.convert_from_path(pdf_path)
#
# pil_im = images[0] # assuming that we're interested in the first page only
#
# ocr_dict = pytesseract.image_to_data(pil_im, lang='eng', output_type=Output.DICT)
# # ocr_dict now holds all the OCR info including text and location on the image
#
# text = " ".join(ocr_dict['text'])
# print(text)



# from PyPDF2 import PdfReader
#
# pdfFileObj = open(r'C:\Users\Unaina\PycharmProjects\pandas1\assesment\imgpdf.pdf','rb')
#
# pdfR = PdfReader(pdfFileObj)
#
# print(pdfR)
#
# pageObj = pdfR.getPage(1)
#
# print(pageObj.extractText())
#
# pdfFileObj.close()


from PyPDF2 import PdfReader
reader = PdfReader(r'C:\Users\Unaina\PycharmProjects\pandas1\assesment\snpdf.pdf')
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)

import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext(r'C:\Users\Unaina\PycharmProjects\pandas1\assesment\snpdf.pdf')
print(result)

import pdfplumber
var = pdfplumber.open(r"C:\Users\Unaina\PycharmProjects\pandas1\assesment\imgpdf.pdf")
print(var.pages[0].extract_text())


