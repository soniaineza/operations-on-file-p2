with open('codingal.txt') as file:
    data1=file.read()

with open('codingal2.txt') as file2:
    data2=file2.read()

data1+="\n"
data1+=data2

print("merging the two files")
with open('codingal3.txt','w') as file3:
    file3.write(data1)

    
