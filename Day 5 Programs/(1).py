def lengthOfLastWord(a):
	b = 0
	x = a.strip()
	for i in range(len(x)):
		if x[i] == " ":
			b = 0
		else:
			b += 1
	return b
a=input("Enter a Sentence")
print("The length of last word is",lengthOfLastWord(a))

