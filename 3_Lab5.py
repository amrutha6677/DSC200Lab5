import csv
import slate3k as sl

filename = "Table9.pdf"

with open(filename, "rb") as fileObj:
    pdfDoc = sl.PDF(fileObj)

    cols = []
    lines = pdfDoc[0].split('\n\n')
    for str_index in range(6, 580, 15):
        cols.append(lines[str_index:str_index+15])

    lines = pdfDoc[1].split('\n\n')
    for str_index in range(7, 560, 15):
        cols.append(lines[str_index:str_index + 15])

    lines = pdfDoc[2].split('\n\n')
    for str_index in range(7, 570, 15):
        cols.append(lines[str_index:str_index + 15])

    lines = pdfDoc[3].split('\n\n')
    for str_index in range(7, 580, 15):
        cols.append(lines[str_index:str_index + 15])

    lines = pdfDoc[4].split('\n\n')
    for str_index in range(7, 570, 15):
        cols.append(lines[str_index:str_index + 15])

    lines = pdfDoc[5].split('\n\n')
    for str_index in range(7, 70, 15):
        cols.append(lines[str_index:str_index + 15])

    for i in range(len(cols)):
        for j in range(len(cols[i])):
            cols[i][j] = cols[i][j].replace('\u2013', '0')
            cols[i][j] = cols[i][j].replace('x', '')
            cols[i][j] = cols[i][j].replace('y', '')
            cols[i][j] = cols[i][j].replace('v', '')
            cols[i][j] = cols[i][j].replace(',', '')
            cols[i][j] = cols[i][j].replace('\n', '')
            cols[i][j] = cols[i][j].strip()

catNames = ['Child labour (%)+ 2005–2012* total', 'Child labour (%)+ 2005–2012* male', 'Child labour (%)+ 2005–2012* female', 'Child marriage (%) 2005–2012* married by 15', 'Child marriage (%) 2005–2012* married by 18', 'Birth registration (%)+ 2005–2012* total', 'Female genital mutilation/cutting (%)+ 2002–2012* prevalence womena  ', 'Female genital mutilation/cutting (%)+ 2002–2012* prevalence girlsb ', 'Female genital mutilation/cutting (%)+ 2002–2012* attitudes support for the practicec', 'Justification of wife beating (%)  2005–2012* male', 'Justification of wife beating (%)  2005–2012* female', 'Violent discipline (%)+ 2005–2012* total', 'Violent discipline (%)+ 2005–2012* male', 'Violent discipline (%)+ 2005–2012* female']

# creates a CSV file
with open('3.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # header row
    csvwriter.writerow(['CountryName', 'CategoryName', 'CategoryTotal'])

    # If the count for any category is zero, that row should not be included in the final dataset.
    # If a country has no entries for a category, do not include that country in the output CSV file.
    for i in range(len(cols)):
        for j in range(len(cols[i])):
            if j == 0:
                continue
            else:
                if cols[i][j] != '0':
                    csvwriter.writerow([cols[i][0], catNames[j-1], cols[i][j]])

# row count in CSV file
with open('3.csv', 'r') as csvfile:
    num_rows = sum(1 for row in csvfile) - 1

# print the number of rows, excluding the header, in the CSV output file
print(f"Number of rows in the CSV file: {num_rows}")

