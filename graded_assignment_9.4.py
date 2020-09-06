#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
file_name = input("Enter file name: ")
file_handle = open(file_name)
counts=dict()

for line in file_handle:
    line=line.strip()
    if line.startswith('From '):
        x=line.split()
        word=x[1]#here when splited we get list there to pick 2nd word x[1] given.
        counts[word]=counts.get(word,0)+1

count=None
word=None
for w,c in counts.items():
    if count is None or c > count:
        word=w
        count=c
print(word,count)
