with open('codingal.txt','w') as file:
    file.write("Hello my name is Sonia")
file.close()

with open('codingal.txt','r') as file:
    data=file.readlines()
    print("the words in the file are:")
    for line in data:
        word=line.split()
        print(word)
file.close()


    