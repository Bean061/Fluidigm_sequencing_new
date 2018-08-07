# -*- coding:utf-8 -*-
f1=open("/Users/zhouwenbin/proj/Test_loci/M50.loci",'r') # open the the .tre file.
s = len(f1.readlines())
f1.close()  #print how many lines are there in the file, which will be used for the loop.
sum = ""
a = 0

f1 = open("/Users/zhouwenbin/proj/Test_loci/M50.loci", 'r')
for n in range(s):
    text = f1.readline()
    if text[0] != "/":
        a = len(text) - 11  ###记得改变数目
        sum = sum + text

    else:
        number = text.find("|")
        number2 = text.rfind("|")
        loci_number = text[number + 1:number2]
        sum = "[Locus" + str(loci_number) + ", " +str(a) + "]" "\n" + sum
        fw = open("/Users/zhouwenbin/proj/Test_loci/M50_loci.nex", 'a')  # you can change your output file name here.
        fw.write(sum)
        fw.close()
        print sum
        sum = ""
f1.close()