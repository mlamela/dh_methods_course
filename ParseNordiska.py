
# coding: utf-8

import re

path = "NordiskaPersonnel.txt"	# The personnel-file
path2 = "BankRegister.txt"	# The complete Bank Register

town_current = []
name_family = []
name_first = []
year_birth = []
language_input = []
education_general = []

with open(path) as file:
	for line in file:
		splitline = re.split("\.\.+", line)
		splitline_names = re.split("\,\s", splitline[0])
		town_current.append(splitline[1].replace("\n", ""))
		name_family.append(splitline_names[0])
		name_first.append(splitline_names[1])

temp = re.sub("[^a-zA-Z]+", "", name_family[0]) 	# first entry in name_family cleared
name_family[0] = temp					# here

with open(path2) as file:
	bank_register = file.read()

# Search the personnel (name_family) in bank_register and include their year of birth (year_birth), language used in the
# Register entry (language_input)

births = [ "synt", "f.+dd" ]
language = [ "Finnish", "Swedish" ]

lower_school = [ "kansakoulu", "folkskola", "elementar", "alkeiskoulu", "jordbruksskola" ]
military_school = [ "kadett" ]
upper_school = [ "lyseo", "gymnasi", "samskola", "tytt.+koulu", "fruntimmerskola", "flickskola" ]
professional_school = [ "realskola", "reaalikoulu", "handelskola", "kauppakoulu", "kauppaopisto" ]
graduate = [ "student", "ylioppila" ]

for i in range(len(name_family)):
	pattern = name_family[i] + ".+" + name_first[i] + ","
	match = re.search(pattern, bank_register)
	if match:
		end = match.end()
#
# Language detected: whether syntynyt or foedd
#
		language_input.append("unknown")
		for birth in births:
			if re.search(birth, bank_register[end:end+50]):
				language_input[i] = language[births.index(birth)]
		if language_input[i] == "unknown":
			print("language not recognised for " + pattern)
#
# Birth year
#
		year = re.search("18\d\d", bank_register[end:])
		start_birth = year.start()+end
		end_birth = year.end()+end
		year_birth.append(bank_register[start_birth:end_birth])
#
# Education: unknown, or: lower_school, military_school, upper_school, professional_school, student
#
		education_general.append("unknown") 				
		# Set unknown to education
		string = " -- "
		education_field = re.search(string, bank_register[end_birth:end_birth+500]) # Detect end of education-field in the register
		if education_field:
			end_education = education_field.end()+end_birth	
		
		else:
			print ("End of field not detected!" + pattern)	
			# Error for debugging
		for education in lower_school:
			if re.search(education, bank_register[end_birth:end_education]):
				education_general[i] = "lower_school"
		for education in military_school:
			if re.search(education, bank_register[end_birth:end_education]):
				education_general[i] = "military_school"
		for education in upper_school:
			if re.search(education, bank_register[end_birth:end_education]):
				education_general[i] = "upper_school"
		for education in professional_school:
			if re.search(education, bank_register[end_birth:end_education]):
				education_general[i] = "professional_school"
		for education in graduate:
			if re.search(education, bank_register[end_birth:end_education]):
				education_general[i] = "student"
	else: 								# Help for debugging, 
		print ("no match, source corrupt:" + pattern)    # manual correction

# Unifying Swedish / Finnish town names

replacement_towns = {
	".+bo$": "abo",
	"turku": "abo",
	"bj.+rneborg": "bjorneborg",
	"pori": "bjorneborg",
	"jyv.+skyl.+": "jyvaskyla",
	"viipuri": "viborg",
	"helsinki": "helsingfors",
	"h.+meenlinna": "tavastehus",
	"hang.+": "hango",
	"hanko": "hango",
	"tampere": "tammerfors",
	"borg.+": "borgo",
	"porvoo": "borgo",
	"k.+kisalmi": "kakisalmi",
	"savonlinna": "nyslott",
	"sordavala": "sortavala",
	"[(].+": "unknown"
	}

def replace_towns(string):
	for key in replacement_towns:
		string = re.sub(key, replacement_towns[key], string)
	return string

for i in range(len(town_current)):
	town_current[i] = town_current[i].replace(" ", "")
	town_current[i] = town_current[i].lower()
	town_current[i] = replace_towns(town_current[i])

#a CSV file created of the list
personnel_list = []
import csv
csv_filename = "Nordiska.csv"
with open(csv_filename, 'w') as f:
	wr = csv.writer(f)
	for i in range(len(town_current)):
		personnel_list = [name_family[i], name_first[i], year_birth[i], town_current[i], education_general[i], language_input[i]]
		wr.writerow(personnel_list)

# Some visualisation!

# 1) stats about language use and education is printed by branch (Helsinki, Abo, Viborg) and per total

towns_studied = ["helsingfors", "abo", "viborg", "villmanstrand", "nyslott"]

def all_language(string1): # string1 = language
    language = 0
    for i in range(len(town_current)):
        if language_input[i] == string1: language+=1
    return language

def all_education(string1): # string1 = education
    education = 0
    for i in range(len(town_current)):
        if education_general[i] == string1: education+=1
    return education

def total_personnel(string):
	total = 0
	for i in range(len(town_current)):
		if town_current[i] == string: total+=1
	return total

def language(string1, string2): # string1 = town, string2 = language (Finnish, Swedish)
	language = 0
	for i in range(len(town_current)):
		if town_current[i] == string1: 
			if language_input[i] == string2: language+=1
	return language

def education(string1, string2): # string1 = town, string2 = education (see above)
	education = 0
	for i in range(len(town_current)):
		if town_current[i] == string1: 
			if education_general[i] == string2: education+=1
	return education

total = len(town_current)
print ("Statistics about the personnel:")
print ("Total: " + str(total))
print ("  language")
print ("Share of entries in Swedish: " + str(all_language("Swedish") / total*100) + " %")
print ("  education")
print ("Share of studenter: " + str(all_education("student") / total*100)+ " %")
print ("Share of professional_school: " + str(all_education("professional_school") / total*100)+ " %")
print ("Share of upper_school: " + str(all_education("upper_school") / total*100)+ " %")
print ("Share of lower_school: " + str(all_education("lower_school") / total*100)+ " %")
print ("-- unknown: " + str(all_education("unknown") / total*100)+ " %")
print ("-------")
print ("Towns studies:")
print (towns_studied)
print ("")
              
for town in towns_studied:
	print ("Personnel in " + town)
	print ("Total personnel: " + str(total_personnel(town)))
	print ("Share of entries in Swedish: " + str(language(town, "Swedish") / total_personnel(town) * 100) + " %")
	print ("Number of studenter: " + str(education(town, "student")))
	print ("Number of professional_school: " + str(education(town, "professional_school")))
	print ("Number of upper_school: " + str(education(town, "upper_school")))
	print ("Number of lower_school: " + str(education(town, "lower_school")))
	print ("")
       
# 2) a graph with personnel per birth year

import matplotlib.pyplot as plt

#get first and last birth years
first = int(year_birth[0])
last = int(year_birth[0])
for i in range(1,len(town_current)):
    if int(year_birth[i]) < first: first = int(year_birth[i])
    if int(year_birth[i]) > last: last = int(year_birth[i])

def births_in_year(string): # string = birth year
    births = 0
    for i in range(len(town_current)):
        if year_birth[i] == string: births+=1
        if year_birth[i] == "1899": print (name_family[i])
    return births

total_birth=[]
x=[]
for year in range(first, last+1):
    total_birth.append(births_in_year(str(year)))
    x.append(year)

print ("Personnel born between: " + str(first) + "--" + str(last))
print (total_birth)

plt.bar(x, total_birth, 2, color="green")
plt.show()

