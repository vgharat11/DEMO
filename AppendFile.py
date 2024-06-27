import os
os.getcwd()
file=open("Append_File.txt","w")
str1="Hello All \n"
str2="How are you all? \n"
str3="Hope all well \n"
file.write(str1)
file.write(str2)
file.write(str3)
file.close()


