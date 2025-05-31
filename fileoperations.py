searchingword = 'is'
occurences = 0
#fw = open('workfile.txt', 'w', encoding="utf-8")
#fw.write('jdhgi')
#fw.close()
fr = open('workfile.txt', 'w+ ', encoding="utf-8")
#read_data = fr.read()
#print(read_data)
for line in fr:
    for word in line.split(' '):
        if word == searchingword:
            occurences = occurences+1
            fw = open('workfile2.txt', 'w', encoding="utf-8")
            fw.write(line)
            fw.close()
print(f"The number of occurences of searching word '{searchingword}' is {occurences}.")
fr.close()

"""fw = open('workfile2.txt', 'w', encoding="utf-8")
fw.write(searchingword)
print()
fw.close()"""
