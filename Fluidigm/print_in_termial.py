import os._exit()

sum1 = ""
for i in range(7):
    cmd = "pyRAD -p params.txt -s " + str(i+1) + " &&"
    sum1 = sum1 + cmd + " "