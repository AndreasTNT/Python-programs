import csv
csvfile = open('patienter.csv', 'w', newline='')
f = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
f.writerow(("Name",'Age','Health','Food'))
f.writerow(('Andreas','11','Bra','Potatis'))
f.writerow(('Julia','5','Bra','Godis'))

csvfile.close

#appendMe ="\nNew bit of information"
#appendFile = open("exampleFile.txt","a+")
#appendFile.write(appendMe)
#appendFile.close()
