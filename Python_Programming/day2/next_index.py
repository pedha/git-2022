str ="It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English."
print(str)
print("\n")
words = str.split(" ")
for i in range(1,len(words),2):
	words[i] = words[i].upper()
print(words)
print(" ".join(words))
