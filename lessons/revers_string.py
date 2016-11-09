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


def reverse(data_list):
    length = len(data_list)
    s = length

    for item in data_list:
        s = s - 1
        data_list[s] = item
    return data_list
