import re

# s = "codestudio: a conding portal for coders"
# match = re.search("portal",s)
# # print("Start Index\t",match.start())
# # print("End Index\t",match.end())

# a = "Conding.Ninja"
# # print(re.search(r".",a))
# # print(re.search(r"\.",a))

# text = "Hello My Name is Aqeel and phone is 123456789 and my friend phone number is 987654321"
# # print(re.findall("\d+",text))

# data = re.compile('[a-e]')
# print(data.findall("aye said mr gaibenson stark"))


pattern = r"[A-Z]+yclone"

text = '''Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in early March 2018. 
Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. 
It became a tropical disturbance on 2 March, and was named the next day after attaining tropical storm status. 
Dumazile reached its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph), 
1-minute sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 
hPa (27.91 inHg). As it tracked southeastwards, Dumazile weakened steadily over the 
next couple of days due to wind shear, and became a post-tropical cyclone on 7 March'''

# match = re.search(pattern, text)
# print(match)

# match = re.finditer(pattern, text)
# for find in match:
#     print(find.span())
#     print(text[find.span()[0]:find.span()[1]])
# #https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions
# # https://regexr.com/

# # Define a regular expression pattern
# pattern = r"expression"

# # Match the pattern against a string
# text = "Hello, world!"

# match = re.search(pattern, text)

# if match:
#     print("Match found!")
# else:
#     print("Match not found.")

# pattern = r"expression"
# text = "The cat is in the hat."

# matches = re.findall(pattern, text)

# print(matches)
# # Output: ['cat', 'hat']
# import re
# pattern = r"[a-z]+at"
# text = "The cat is in the hat."

# matches = re.findall(pattern, text)

# print(matches)
# # Output: ['cat', 'hat']

# new_text = re.sub(pattern, "dog", text)

# print(new_text)
# # Output: "The dog is in the dog."

# import re

# text = "The email address is example@example.com."

# pattern = r"\w+@\w+\.\w+"

# match = re.search(pattern, text)

# if match:
#     email = match.group()
#     print(email)
# Output: example@example.com     