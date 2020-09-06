# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
file_name=input("Enter file name:")
file_handle=open(file_name)
lst=list()
for line in file_handle:
    line=line.rstrip()#it removes the space in the line
    line=line.split()#split takes the string and gives list
    for words in line:
        if not words in lst:#if the word is not in the list it adds it.
            lst.append(words)
lst.sort()
print(lst)
