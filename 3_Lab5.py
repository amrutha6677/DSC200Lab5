import PyPDF2 as pypdf
import slate3k as sl

filename = "Table9.pdf"

with open(filename, "rb") as fileObj:
    pdfDoc = sl.PDF(fileObj)

    for page in pdfDoc:
        print(page)
#
# with open(filename, "rb") as pdfFile:
#     reader = pypdf.PdfReader(pdfFile)
#
#     unformatText = []
#
#     for page in reader.pages:
#         text = page.extract_text()
#         unformatLine = []
#         for line in text.split('\n'):
#             current = line.replace('\u2013', '0')
#             prev = ''
#             index = 0
#             for letter in text:
#                 if prev in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
#                     newLine = current[:index]
#
#                     index += 1
#                 # elif letter == '  ':
#                 #     current = current[:index] + ',' + current[index+1:]
#                 #     index += 1
#                 else:
#                     index += 1
#                 prev = letter
#             current = current.replace(' ', ',')
#             unformatText.append(current)
#
#     print(unformatText)
