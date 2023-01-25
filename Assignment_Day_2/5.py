filename = "hash.txt"
with open(filename) as filedata:
    ch = filedata.read()
with open(filename, "w") as filedata:
    for word in ch:
        print(word + "#",end="", file=filedata)