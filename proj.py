import csv
import sys

#create array to put attributes into
data_array= []
#array for classes
class_array= []

#open pordate file
f=open("pordate.csv", "r")
reader=csv.reader(f)

#go through data file and create arrays of 0 and 1's for each student (breakdown on google docs)

for row in reader:
	
	tmp= []
	cmp=[]
	#male or female
	if(row[0]=='F'):
		tmp.extend([0,1])
	elif(row[0]=='M'):
		tmp.extend([1,0])
	else:
		#this for first line with headers
		continue
	#age 15-22
	if(row[1]=='15'):
		tmp.extend([1,0,0,0,0,0,0,0])
	elif(row[1]=='16'):
		tmp.extend([0,1,0,0,0,0,0,0])
	elif(row[1]=='17'):
		tmp.extend([0,0,1,0,0,0,0,0])
	elif(row[1]=='18'):
		tmp.extend([0,0,0,1,0,0,0,0])
	elif(row[1]=='19'):
		tmp.extend([0,0,0,0,1,0,0,0])
	elif(row[1]=='20'):
		tmp.extend([0,0,0,0,0,1,0,0])
	elif(row[1]=='21'):
		tmp.extend([0,0,0,0,0,0,1,0])
	else:
		tmp.extend([0,0,0,0,0,0,0,1])
	#study time 1-4
	if(row[2]=='1'):
		tmp.extend([1,0,0,0])
	elif(row[2]=='2'):
		tmp.extend([0,1,0,0])
	elif(row[2]=='3'):
		tmp.extend([0,0,1,0])
	else:
		tmp.extend([0,0,0,1])
	#failure 0-4
	if(row[3]=='0'):
		tmp.extend([1,0,0,0,0])
	elif(row[3]=='1'):
		tmp.extend([0,1,0,0,0])
	elif(row[3]=='2'):
		tmp.extend([0,0,1,0,0])
	elif(row[3]=='3'):
		tmp.extend([0,0,0,1,0])
	else:
		tmp.extend([0,0,0, 0,1])
	#activites yes or no
	if(row[4]=='yes'):
		tmp.extend([1,0])
	else:
		tmp.extend([0,1])
	#Higher yes or no
	if(row[5]=='yes'):
		tmp.extend([1,0])
	else:
		tmp.extend([0,1])
	#romantic yes or no
	if(row[6]=='yes'):
		tmp.extend([1,0])
	else:
		tmp.extend([0,1])
	#Fam rel 1-5
	if(row[7]=='1'):
		tmp.extend([1,0,0,0,0])
	elif(row[7]=='2'):
		tmp.extend([0,1,0,0,0])
	elif(row[7]=='3'):
		tmp.extend([0,0,1,0,0])
	elif(row[7]=='4'):
		tmp.extend([0,0,0,1,0])
	else:
		tmp.extend([0,0,0, 0,1])
	#Free time 1-5
	if(row[8]=='1'):
		tmp.extend([1,0,0,0,0])
	elif(row[8]=='2'):
		tmp.extend([0,1,0,0,0])
	elif(row[8]=='3'):
		tmp.extend([0,0,1,0,0])
	elif(row[8]=='4'):
		tmp.extend([0,0,0,1,0])
	else:
		tmp.extend([0,0,0, 0,1])
	#Goout  1-5
	if(row[9]=='1'):
		tmp.extend([1,0,0,0,0])
	elif(row[9]=='2'):
		tmp.extend([0,1,0,0,0])
	elif(row[9]=='3'):
		tmp.extend([0,0,1,0,0])
	elif(row[9]=='4'):
		tmp.extend([0,0,0,1,0])
	else:
		tmp.extend([0,0,0, 0,1])
	#absences 1-5
	if(row[10]=='1'):
		tmp.extend([1,0,0,0,0])
	elif(row[10]=='2'):
		tmp.extend([0,1,0,0,0])
	elif(row[10]=='3'):
		tmp.extend([0,0,1,0,0])
	elif(row[10]=='4'):
		tmp.extend([0,0,0,1,0])
	else:
		tmp.extend([0,0,0, 0,1])
	#G3 1-3 into class array
	if(row[11]=='1'):
		cmp.extend([1,0,0])
	elif(row[11]=='2'):
		cmp.extend([0,1,0])
	else:
		cmp.extend([0,0,1])
	
	#add student to big arrays
	data_array.append(tmp)
	class_array.append(cmp)

#close file	
f.close()