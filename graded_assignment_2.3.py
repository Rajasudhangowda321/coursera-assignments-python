# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.
hour = input("Enter Hours:")#Enter the hours
flt_hour=float(hour)#converting string to float
rate=input("Enter rate:")#Enter the rate per hour
flt_rate=float(rate)#converting string to float
grosspay=flt_hour*flt_rate#multiplication of hour and rate
print("Pay:",grosspay)
