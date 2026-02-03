s = " a man ,a plan, a canal: panama"
s = "Yo! Banana Boy!"
#step 1: remove punctuation
# step 2: remove spaces
#step 3: convert to upper/lower case
#step 4: compare with the reversed
# step 5: profit!

punctuation = "!,.?-"
for p in punctuation:
    s = s.replace(p, "")
print(s)
s = s.lower()
print(s)
if s == s[::-1]:
    print("IS a palindrome")
else:
    print("NOT a palindrome")
