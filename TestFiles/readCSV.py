text = "Hej Andreas. Sample Text to Save\nNew line!"
import csv

saveFile = open("exampleFile.txt","w")
saveFile.write(text)
saveFile.close()

csvfile = open('patienter.csv', 'r')
patientsObj= csv.reader(csvfile)
for row in patientsObj:
	print('Row #' + str(patientsObj.line_num) + ' ' + str(row))
csvfile.close


