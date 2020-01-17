import csv
import tabula
import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def parse_pdf():
	# tabula.convert_into("A_Threat_Actor_Encyclopedia.pdf", "output.csv", output_format="csv", pages='all')
	# pdfFileObj = open('A_Threat_Actor_Encyclopedia.pdf', 'rb') 
	# pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
	# for i in range(0, pdfReader.numPages):
		# print(pdfReader.getPage(i).extractText())
	# pdfFileObj.close() 	
	# tabula.convert_into("A_Threat_Actor_Encyclopedia.pdf", "output.json", output_format="json", pages='all') #this method has promise
	df = tabula.read_pdf('A_Threat_Actor_Encyclopedia.pdf', pages='7', multiple_tables=True)
	foundNameSection = False
	for line in df:
		for i, row in line.iterrows():
			print(row[0], row[1])

	# for line in df:
	# 	if line == 'Names':
	# 		foundNameSection = True
	# 	elif foundNameSection:
	# 		print(line)
	# 		if line == 'Country':
	# 			foundNameSection = False
	# print(df)
	# tabula.convert_into("A_Threat_Actor_Encyclopedia.pdf", "output.json", output_format="json", pages='all') #this method has promise


def convert_csv_to_json():
    with open('A_Threat_Actor_Encyclopedia.csv') as csv_file:
        in_name_section = False
        csv_reader = csv.reader(csv_file, delimiter=',')
        names = []
        for row in csv_reader:
            if in_name_section:
                if row[0] == 'Country':
                    in_name_section = False
                else:
                    if row[1] != "":
                        names.append(row[1])
            elif row[0] == 'Names':
                if row[1] != "":
                    names.append(row[1])
                    in_name_section = True
            # elif row[0].startswith('Names') or row[1].startswith('Names'):
            #     in_name_section = True
            #     continue
        print(names)

if __name__ == '__main__':
	parse_pdf()
    # convert_csv_to_json()

