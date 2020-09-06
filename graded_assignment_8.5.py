#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
file_name = input("Enter file name: ")
file_handle = open(file_name)
count = 0
for line in file_handle:
    line=line.strip()
    if line.startswith('From '):
        count+=1
        x=line.split()
        word=x[1]
        print(word)
print("There were", count, "lines in the file with From as the first word")
