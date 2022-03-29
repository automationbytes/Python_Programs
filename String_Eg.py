import random
import string

s1 = "Hello"
print(type(s1))
s2 = 'H'
print(type(s2))

s3 = '''Python is a high-level, 
general-purpose programming language. 
Its design philosophy emphasizes code readability 
with the use of significant indentation. 
Its language constructs and object-oriented 
approach aim to help programmers write clear, 
logical code for small- and large-scale project'''
print(s3)

"""Python is a high-level, 
general-purpose programming language. 
Its design philosophy emphasizes code readability 
with the use of significant indentation. 
Its language constructs and object-oriented 
approach aim to help programmers write clear, 
logical code for small- and large-scale project"""

fruit = "MANGO IS A SWEETEST FRUIT"
print(len(fruit))
#indexing
print(fruit[1])
#negative indexing
print(fruit[-3])

#slicing

print(fruit[11:19])
#negative slicing
print(fruit[-14:-6])

print(fruit[11:])
print(fruit[:11])

#STRIP - used to trim the whitespaces both in front n back
a = "   Hello   world   "
print(a.strip())
print(len(a.strip()))
#lstrip - left trim the whitespaces
print(a.lstrip())
print(len(a.lstrip()))
#rstrip - right trim
print(a.rstrip())

#lower case
a = "HELLO"
print(a.lower())
print(a.casefold())
b = "hello"
print(b.upper())
c = "python is easiest language"
print(c.capitalize())
print(c.title())

z = "GRAß"
print(z.lower())
print(z.casefold())

y = "Python Is Easiest Language"
#print(y.swapcase())

#replace
print(y.replace("Easiest","Hardest"))

#split
li = y.split(" ")
print(li)
print(li[0])
print(li[-2])
li[-2] = "Hardest"
print(li)

print("ang" in y)

a = "hello"
b = "world"
c= 5
print(a+b+str(c))
print(a+b+format(c))

a = "apple"
print(a.center(20,"*"))

a = "I love apple, apple is most popular fruit. even apple has phones under its name"
print(a.count("apple",10,35))
print(a.endswith("name"))
print(a.find("apple"))

abc = ['Python', 'Is', 'Hardest', 'Language']
str = " ".join(abc)
print(str)

d = {65:69}
a = "APPLE"
print(a.translate(d))
print(a.replace("A","E"))

t = "6549"
print(t.zfill(10))

random_name = ''.join(random.sample(string.ascii_letters,5))  #string.ascii_lowercase or string.digits
print(random_name)

