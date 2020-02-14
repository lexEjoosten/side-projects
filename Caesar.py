def c(n,s):
	o=""
	for i in range(0,len(s)):
		if s[i]!=" ":
			o=o+str(chr(97+((n+(ord(s[i])-96))%25)))
		else:
			o=o+" "
	return o

def test():
	print("yes")

def letter_to_number(string):
	n=""
	for l in string:
		n=n+"p"