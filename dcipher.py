s,o=str(input(" ")),""
import Caesar
for p in range(0,len(s)):
	if (ord("A")<=ord(s[p])<=ord("Z")):
		o=o+chr(ord(s[p])-(ord("A")-ord("a")))
	elif s[p]=="." or s[p]=="," or s[p]=="!" or s[p]=="'" or s[p]=="\"":
		u=0
	else:
		o=o+s[p]
s=o
n=s[0]
for p in range(1, len(s)):
	if (s[p]==" "):
		n=n+" "
	elif (s[p-1]==" "):
		n=n+str(chr(97+(((-1*(ord(*n[p-2])-96))+(ord(s[p])-96))%25)))
	else:
		n=n+str(chr(97+(((-1*(ord(n[p-1])-96))+(ord(s[p])-96))%25)))
print(n)
oi=input()