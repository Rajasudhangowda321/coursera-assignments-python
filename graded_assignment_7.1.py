#Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
file_name=input("enter the file name:")
r=open(file_name)
x=r.read().strip()
print(x.upper())
