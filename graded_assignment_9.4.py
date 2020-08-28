#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fname = input("Enter file name: ")
fh = open(fname)
counts=dict()

for line in fh:
    line=line.strip()
    if line.startswith('From '):
        li=line.split()
        word=li[1]
        counts[word]=counts.get(word,0)+1

c=None
w=None
for word,count in counts.items():
    if c is None or count > c:
        w=word
        c=count
print(w,c)
