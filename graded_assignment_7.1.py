#Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
fname=input("enter the file name:")
o=open(fname)
r=o.read().strip()
print(r.upper())
