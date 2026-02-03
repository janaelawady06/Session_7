# + will perform string concatenation
s1 = "hello"
s2 = "bye"
print(s1+s2)
print(s2+s1)
print(s1+" "+s2+"!!")

#you cab multiply a string by an integer
print(3*s2) #nsync song

#we can iterate over a string using for
# 1. do the same with a while
# 2. i want the result to be hellloooo
for c in s1:
    print(c)

i = 0
while i < len(s1):
    print(s1[i])
    i += 1

s_new = ("")
for c in s1:
    s_new = s_new + c*4
int(s_new)


