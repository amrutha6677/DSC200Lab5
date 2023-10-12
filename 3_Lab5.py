import PyPDF2 as pypdf

filename = "Table9.pdf"

with open(filename, "rb") as pdfFile:
    reader = pypdf.PdfReader(pdfFile)

    print(len(reader.pages))

    for page in reader.pages:
        page = page.extract_text()
        print(page)