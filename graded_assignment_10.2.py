#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
file=input("Enter a file name:")
handle=open(file)
count=dict()
for line in handle:
    if line.startswith('From '):
        l=line.split()
        u=l[5].split(':')#here double split is done
        u=u[0]
        count[u]=count.get(u,0)+1
        s=sorted([(k,v)for k,v in count.items()])
for k,v in s:
    print(k,v)
