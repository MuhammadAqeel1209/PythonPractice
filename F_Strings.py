data = "My Name is {} And I am from {}"
country = "PAKISTAN"
name = "AQEEL"

namelist = []
countrylist = []

namelist.append("Ali")
namelist.append("Ahmad")
namelist.append("Faheem")
namelist.append("Asad")

countrylist.append("Lahore")
countrylist.append("Rawalpindi")
countrylist.append("Karachi")
countrylist.append("Faisalabad")



#print(data.format(name,country))

for i in namelist:
    for j in countrylist:
       print(f"My Name is {namelist} And I am from {countrylist}")

# print(f"My Name is {name} And I am from {country}")
# print(f"My Name is{{name}} And I am from {{country}}")