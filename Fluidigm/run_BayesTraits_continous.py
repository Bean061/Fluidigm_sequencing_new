

filename = "/Users/zhouwenbin/tools/BayesTraits/test_conti/Bioclim" + str(1) + ".txt.Stones.txt"
filename1 = "/Users/zhouwenbin/tools/BayesTraits/test_conti/output.txt"
f1=open(filename,'r') # open the the .tre file.
s = len(f1.readlines())
f1.close()

f1=open(filename,'r')
lines = f1.readlines()
sum = lines[int(s-1)]
f2=open(filename1,'a')
f2.write(sum)
f2.close()

f1.close()