str2 = "adilav"[::-1]
str1 = "on"
str3 = "ti"
print "Selected first word: ", str2 + str3 + str1

sentx = {
	str2: "adilav",
	str1: "on",
	str3: "ti"
	}

print "Selected second word: ", sentx[str2][::-1] + sentx[str3] + sentx[str1]