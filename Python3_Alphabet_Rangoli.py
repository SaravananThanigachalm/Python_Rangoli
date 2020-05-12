""" Python 3 programming for an alphabet Rangoli """


import string  # This imports the string libary that contains all charaters

a = list(string.ascii_lowercase) # Makes a list of lowercase letter and asign to a
n = int(input("Enter the value upto which alphabet the Rangoli need to be printed\n"))
# Note the maximum value is 27 as the number alphabets is 27
b = []
for i in range(n):
    c = "-".join(a[i:n])
    b.append((c[::-1]+c[1:]).center(4*n-3,"-"))
print('\n'.join(b[:0:-1]+b))
    


