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

# -----------------------------------------------------------------------------------

def reverse1(data_list): 
    length = len(data_list) 
    s = length 
    
    new_list = [None]*length
    
    for item in data_list: 
        s = s - 1 
        data_list[s] = item 
    return data_list
# -----------------------------------------------------------------------------------

def reverse_a_string_more_slowly(data_list):
    new_strings = []
    index = len(data_list)
    while index:
        index -= 1                       
        new_strings.append(data_list[index])
    return ''.join(new_strings)

# -----------------------------------------------------------------------------------
def reverse2(data_list):  # Slice Method
	return data_list[::-1]
# -----------------------------------------------------------------------------------

print reverse_a_string_more_slowly('tseb uoy')
	
print reverse2('tseb uoy')