#upper()
name = "lokesh loki"
print(name.upper())

#lower()
a = "LOKESH"
print(a.lower())

#swapcase()
s = "Python class"
print(s.swapcase())

#capitalize()
q = "hello world"
print(q.capitalize())

#title()
word = "hello welcome to python automation"
print(word.title())

#strip()
b = "  python rocks    "
print(b.strip())

#lstrip()
c = "  lokesh"
print(c.lstrip())

#rstrip()
d = "  loki    "
print(d.rstrip())

#replace()
e = "lokesh loki"
print(e.replace("loki","savvy"))

#index() returns the index of the first occurance of the string searched
print(e.index("lokesh"))

#find() returns the index of the firat occurence of the substring in a string
print(e.find("savvy"))
print(e.find("loki"))

#count()
o = "lokesh loki"
print(o.count("l"))
print(o.count('o'))

#startswith()
print(o.startswith("lo"))

#endswith()
print(o.endswith("ki"))
print(o.endswith("lo"))

#isalnum(), isalpha(), isdigit(), islower(), isupper(), isspace()
r = "loki 1435"
print(r.isalnum())
print(r.isalpha())
print(r.isdigit())
print(r.islower())
print(r.isupper())
print(r.isspace())



