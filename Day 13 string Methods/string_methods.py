#Strings are immutable 
a="!!Antima!!!!! Antima"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Antima","Anu"))
print(a.split(" "))

blogHeading="Intro to python "
print(blogHeading.capitalize())

str1="Welcome to the console!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Antima"))
 
str1="Welcome to the Console !!"
print(str1.endswith("!!"))

str1="welcome to the console !!"
print(str1.endswith("to",4,10))

#index() and find() are work similar but in case index it will give error or in case find it will give -1
str1="She is so bootiful and always in my heart "
print(str1.find("is"))
print(str1.index("is"))
#print(str1.index("ish"))

str1="WelcomeTOThe Console"
print(str1.isalnum())

str1="Welcome"
print(str1.isalpha())

str1="hello world"
print(str1.islower())

str1="We wish you are merry chirstmas"
print(str1.isprintable())

str2="      "
print(str2.isspace())

str1="World  Health Organization"
print(str1.istitle())

str2="To  kills a mocking bird"
print(str2.istitle())

str1="Python is a Interpreted Langauge "
print(str1.startswith("Python"))

str1="Python is Interpreted Langauge "
print(str1.swapcase())

str1="His name is Dan ,Dan is an honest man "
print(str1.title())







