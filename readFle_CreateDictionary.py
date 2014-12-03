def read():
    res = {}
    with open("text.txt","r") as text:
        for line in text:
            key, value = line.split()
            if int(value) > res.get(key, -1):
                res[key] = int(value)
    return res
