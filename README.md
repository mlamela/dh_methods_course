# dh_methods_course: processing a register of bank personnel

DH methods course project: the personnel of the Finnish Nordiska Aktiebanken in the early 20th century

[![DOI](https://zenodo.org/badge/77734274.svg)](https://zenodo.org/badge/latestdoi/77734274)

GENERAL

This is a course project for the Methods in DH (HELDIG) and investigates the biographic information of the people working in the Finnish bank Nordiska Aktiebanken för Handel och Industri (NAB, founded in 1873) in the beginning of the 20th century. 

In general, the scholarship of Finnish banking history has paid attention mainly to the companies and their key personnel, not the people working in the banks as such. Moreover, even though a major player of its time, the NAB is less well studied as it merged in 1919 with the Föreningsbanken i Finland (the country's first commercial bank founded in 1862). This course exercise analyses biographic data in the Bank Register compiled by A. Markkula (Bankmatrikel för Finland : biografiska uppgifter angående tjänstepersonalen vid bankinrättningar I Finland, 1909). This Register is based on the biographic details provided by the personnel themselves, and includes, thus, a variety of information.

FILES INCLUDED

-Bankregister.txt – Automatically read file, partly manually corrected, of the Bank Register (1909)

-BankRegisterExample.jpg – An example page of the Bankmatrikel by A. Markkula (1909)

-NordiskaPersonnel.txt – The personnel of the Nordisk Aktiebanken, from the index of the Bankmatrikel (1909), manually corrected

-ParseNordiska.py – Python programme, which combines the data found in the Bankregister.txt to the personnel of the Nordiska Aktiebanken. The results are stored in a new file (Nordiska.csv), and the information is visualised.

PROJECT DESCRIPTION

i) An OCR file of the 1909 Bank Register was created and processed. An example file of the original document is BankRegisterExample.jpg. There were major problems with the OCR due to the weak quality of the digitalised images (example page is included, BankRegisterexample.jpg). The list of the personnel of the Nordiska Aktiebanken was corrected manually (NordiskaPersonnel.txt), and the names in the Bank Register were checked manually (BankRegister.txt).

ii) The python programme (ParseNordiska.py) picks data related to the personnel of the Nordiska Aktiebanken from the Bank Register: name, birth year, current town of residence, education. Also, the programme consideres which language (Swedish or Finnish) the person has used in his biographical entry. The data collected is printed into a csv-file (Nordiska.csv). Finally, the programme visualises the combined data by total and by selected bank branches.

USAGE (ParseNordiska.py)

-requires matplotlib

-place NordiskaPersonnel.txt and BankRegister.txt in the same folder

-run: python ParseNordiska.py

RESULTS AND FURTHER DEVELOPMENT

The results are at this stage very preliminary due to the weak quality of the OCR. The results confirm some previous observations, for example, that the NAB had a Swedish-speaking identity. However, more information is needed about the educational choices and previous professional careers of the employees. The graph shows that the personnel of the bank was rather young: two major age groups are found, those in their late thirties and those under thirty. This probable relates to the position of the employee in the bank hierarchy. The analysis could benefit of comparison with the personnel of the other banks.

The project will be developed in two ways: first, the Bank Register needs to be digitised again directly from the printed version. In this way also other banks than NAB can be included to the study, and the more detailed biographic data can be used. Second, more data should be collected from the Bank Register. There are certain difficulties related to this, as the format of the entries varies a bit according to the information the person has submitted. Moreover, the results need to be visualised in a better way by using maps and presenting the data in time (career paths of the employees).
