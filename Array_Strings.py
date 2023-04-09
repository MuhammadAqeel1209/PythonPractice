#CHARCTER ARRAY  COLLECTION OF ITEMS
#STRINGS ARE IMMUTABLE(DOES NOT CHANGE THE STRING BUT MAKE A COPY OF STRINGS LIKE UPPER,LOWER ETC)
name = "AQEEL    !!!!!!!!";
stringLong = "I AM AQEEL\tGOOD BYE 012\t"
# print(name[0]);
# print(name[1]);
# print(name[2]);
# print(name[3]);
# print(name[4]);

# FOR LOOP 
# for character in stringLong:
#     print(character)
"""
names = "MUHAMMAD AQEEL SHAKEEL"
print(names[9:15])
print(len(names)) # LENGTH OF ARRAYS
print(names[0:-9]) #print(names[0:len(names)-9])

nm = "HARRY"
print(nm[-4:-2])
"""

frdName = "Faran Ehtsham Aqeel Ahsan Aqeel"
#----------------------------UPPER METHOD----------------------------
"""UPPER THE ALL CASE"""
# print(frdName.upper())

#----------------------------LOWER METHOD----------------------------
"""LOWER THE ALL CASE"""
# print(name.lower())

#----------------------------RSTRIP METHOD----------------------------
"""REMOVE "!" ANY "TRAILLING" CHARACTER AFTER THE NAMES """
#print(name.rstrip("!")) 

#----------------------------REPLACEMETHOD----------------------------
"""REPLACE USED TO REPLACE ALL OCCURANCE OF STRINGS WITH OTHER STRINGS"""
# print(name.replace("AQEEL","MUHAMMAD AQEEL"))

#----------------------------SPLIT METHOD----------------------------
"""SPLIT USED TO CONVERT THE STRING TO LIST """
#print(frdName.split(" "))

#----------------------------CAPITILIZE METHOD----------------------------
"""CAPITILIZE USED TO CONVERT THE FIRST CHARACTER OF STRING IN CAPITAL AND
 CONVERT OTHER CHARACTER OF STRING IN LOWER"""
#heading = "aqeel"
# print(heading.capitalize())
# heading2 = "aqEEl"
# print(heading2.capitalize())

#----------------------------CENTRE METHOD----------------------------
"""CENTER METHOD USED TO ALLIGN THE STRING IN CENTRE"""
# str1 = "WELCOME TO THE PYTHON SCRIPT"
# print(str1.center(50))
# print(len(str1))
# print(len(str1.center(50)))

#----------------------------COUNT METHOD----------------------------
"""COUNT USED TO COUNT THE GIVEN VALUES IN STRINGS"""
# print(frdName.count("Aqeel"))

#----------------------------END SWITCH METHOD----------------------------
"""ENDSWITCH METHOD IS USED TO CHECK IF THE STRING END WITH SPECIAL CHARACTER OR NOT"""
# print(name.endswith("!"))
# print(frdName.endswith("!"))

#----------------------------FIND METHOD----------------------------
"""
FIND METHOD USED TO FIND THE FIRST OCCURANCE OF SPECIFIC VALUES AND RETURN THE INDEX WHERE IT IS PRESENT
IF THE GIVEN VALUES ABSENT FROM THE STRING WHICH RETURN -1 """
# print(frdName.find("n"))
# print(frdName.find("zz"))

#----------------------------ISALNUM METHOD----------------------------
""" ISALNUM USED TO IDENTIFY THE ALPHA NUMBERIC STRING A-Z,a-z,0-9
OTHER WISE RETURN FALSE """
# print(frdName.isalnum())
# print(name.isalnum())
# print(stringLong.isalnum())

#----------------------------ISALPHA METHOD----------------------------
""" ISALPHA USED TO IDENTIFY THE ALPHA STRING A-Z,a-z OTHER WISE RETURN FALSE """
# print(frdName.isalpha())
# print(stringLong.isalpha())

#----------------------------ISLOWER METHOD----------------------------
""" ISLOWER USED TO IDENTIFY THE LOWER STRING a-z OTHER WISE RETURN FALSE """
# print(heading.islower())
# print(frdName.islower())

#----------------------------PRINTABLE METHOD----------------------------
"""PRINTABLE IDENTIFY THE PRINTABLE CHRACTER """
# print(frdName.isprintable())
# print(stringLong.isprintable())

#----------------------------ISSPACE METHOD----------------------------
""" ISSAPCE IDENTIFY THE SPACE  -->Doule tab space exit then return true otherwise"""
# strSpace = "\t\t"
# print(strSpace.isspace())
#print(frdName.isspace())
# print(name.isspace())
# print(stringLong.isspace())

#----------------------------IS TITILE METHOD----------------------------
""" ISTITLE USED TO IDENTIFY THE CAPITAL LETTER OF EACH WORD IN THE STRING """
# print(frdName.istitle())
# print(stringLong.istitle())

#----------------------------START WITH METHOD----------------------------
"""STARTWITH METHOD IS USED TO CHECK IF THE STRING STRAT WITH SPECIAL CHARACTER OR NOT"""
# str2 = "Python is Programing language"
# print(str2.startswith("Python"))
# print(frdName.startswith("F"))
# print(name.startswith("!!"))

#----------------------------SWAPCASE METHOD----------------------------
"""SWAP CASE SWAP THE ALL CASE"""
# print(frdName.swapcase())

#----------------------------END----------------------------