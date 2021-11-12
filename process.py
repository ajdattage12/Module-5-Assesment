# log_file = open("um-server-01.txt")
 #This line of code opens the file 'um-server-01.txt' and sets it to a variable called
 #log_file

# def sales_reports(log_file): 
#This line of code is defining a function called sales_reports and it is going to accept one
#param. In this case the log_file
    # for line in log_file:
#This line of code is using a 'for in' loop to iterate over log_file
        # line = line.rstrip()
#This line of code strips or removes any trailing characters from a string
        # day = line[0:3]
#This line of code specificies a location
        # if day == "Tue":
#This line of code is an 'if' statement and will check to see if the value of day is == "Tue"
            # print(line)
# sales_reports(log_file)
#this line of code calls and invokes the function 'sales_reports' with 'log_file'

#there should be an extra line of code at the end.
#log_file.close()

log_file = open("um-server-01.txt")

def sales_reports(log_file): 
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)
# sales_reports(log_file)

# log_file.close()

# In process.py, write another function that prints
# out all the melon orders that delivered over 10 melons.

def melon_delivery(log_file):
    for line in log_file:
        line = line.strip()
        line = line.split(' ')
        amount = int(line[2])
        if amount > 10:
            print(' '.join(line))

melon_delivery(log_file)
