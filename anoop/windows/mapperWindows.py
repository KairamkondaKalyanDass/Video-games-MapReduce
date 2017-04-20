f = open("VideoGames.txt","r")
o = open("intermediateOutput.txt","w")
salesTotal = 0.0

for line in f:
    data = line.strip().split("\t")
    if len(data) == 16:
        #name, platform, year, genre, publisher, nasales, eusales, jpsales, othersales, globalsales, criticScore, criticCount, userScore, userCount, developer,rating = data
		salesTotal = float(data[5])+ float(data[6])+ float(data[7])+ float(data[8])+ float(data[9])
		print "{0}\t{1}".format(data[1], salesTotal)
		o.write("{0}\t{1}\n".format(data[1], salesTotal))
		
# Nintendo         165.07 (Key value pair)

f.close()
o.close()

new = open("intermediateOutput.txt","r")
full = open("tempOutput.txt","w")
lines= new.readlines()
lines.sort()
salesTotal = 0.0
oldKey = None
print(lines)
for line in lines:
	data_mapped = line.strip().split("\t")
	if oldKey and oldKey != data_mapped[0]:
		print oldKey, "\t", salesTotal
		full.write("{0}\t{1}\n".format(oldKey, salesTotal))
		oldKey = data_mapped[0]
		salesTotal = 0.0
	oldKey = data_mapped[0]
	salesTotal += float(data_mapped[1])

if oldKey != None:
	print oldKey, "\t", salesTotal
	full.write("{0}\t{1}\n".format(oldKey, salesTotal))
new.close()
full.close()
