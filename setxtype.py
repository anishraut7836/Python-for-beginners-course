s={10,20,30,"xyz"}
print(s)
print(type(s))

#set don't add dupulicate value
s={10,20,30,"xyz", 10, 20, 30}
print(s)
print(type(s))

#add value using update

s={10,20,30,"xyz"}
s.update[(88,99)]
print(s)
print(type(s))

#remove value
s={10,20,30,"xyz"}
s.remove[(30)]
print(s)
print(type(s))


#frozenset
s={10,20,30,"xyz"}
f=frozenset(s)
f.remove(20)

