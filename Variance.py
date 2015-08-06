import os, sys

def main():
	fName = sys.argv[1]

	fl = open(fName, "r")

	for line in fl:
		line = line.strip()
		line = line.split("\t")

		variance = ((float(line[5])*((1-float(line[12]))*(1-float(line[12]))))+(float(line[6])*((2-float(line[12]))*(2-float(line[12]))))+(float(line[7])*((3-float(line[12]))*(3-float(line[12]))))+(float(line[8])*((4-float(line[12]))*(4-float(line[12]))))+(float(line[9])*((5-float(line[12]))*(5-float(line[12])))))/(int(line[11])-1)

		print line[0]+"\t"+line[1]+"\t"+line[2]+"\t"+line[3]+"\t"+line[4]+"\t"+line[5]+"\t"+line[6]+"\t"+line[7]+"\t"+line[8]+"\t"+line[9]+"\t"+line[10]+"\t"+line[11]+"\t"+line[12]+"\t"+str(variance)+"\t"+str(float(line[12])-variance)+"\t"+line[13]+"\t"+line[14]
	
	fl.close()




if __name__ == "__main__":
	main()

