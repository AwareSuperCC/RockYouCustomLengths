num=int(input('Enter minimum character length of password: '))
name="rockyou"+str(num)+".txt"
file=open("rockyou.txt",'r',encoding='latin-1')
newfile=open(name,"w",encoding='latin-1')
lines=file.readlines()
for line in lines:
    if len(line)>=(num+1): #accounts for \n character
        newfile.write(line)
file.close()
newfile.close()
print('done')
