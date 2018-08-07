import os

for i in range(56):
    inputname= "/Users/zhouwenbin/proj/nex/Locus" + str(i) +".phy"
    outputname="/Users/zhouwenbin/proj/jmodel/Locus" +str(i)
    if os.path.isfile(inputname) == True:
        cmd1 = "java -jar /Users/zhouwenbin/tools/jModelTest-2.1.4/jModelTest.jar -d " + inputname + " -g 4 -i -f -AIC -a -o " + outputname
        os.system(cmd1)
