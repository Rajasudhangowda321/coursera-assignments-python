# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
hour=input("Enter hours:")#Enter the hours
flt_hour=float(hour)#converting string to float
rate=input("Enter rate:")#Enter the rate per hour
flt_rate=float(rate)#converting string to float
if flt_hour <= 40:#this condition works if input hour is lessthan 40
    print(flt_hour*flt_rate)
else :#this condition works if input hour is morethan 40 and the rate should be 1.5 times more only if hour is morethan 40
    print((40*flt_rate)+(flt_hour-40)*flt_rate*1.5)#Observation:flt_hour-40 is if hour morethan 40 will be subtracted and the rate will be multiplied 1.5 times more
