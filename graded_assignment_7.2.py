# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# Use the file name mbox-short.txt as the file name
file_name = input("Enter file name: ")
file_handle= open(file_name)
count=0
total=0
for line in file_handle:
    if not line.startswith("X-DSPAM-Confidence: ") :
        continue
    count+=1
    count=float(count)
    x=line[20:]
    total=float(x)+float(total)
print("Average spam confidence:",total/count)
