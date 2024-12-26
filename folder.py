file=open('student.txt','x')
file.close()

import os
print("checking if the file exist or not")
if os.path.exists('student1.txt'):
    os.remove('student1.txt')
else:
    print("the file doesnot exist")
file=open('studen1.txt','w')
file.write("Hello Im a Student")
file.close()
os.remove('codingal.txt')
os.rmdir('stude')