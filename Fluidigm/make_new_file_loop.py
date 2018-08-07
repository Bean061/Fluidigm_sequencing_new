import os
for i in range(20):
    print i
    inputname= "/Users/zhouwenbin/Downloads/Ancestral\ construction/BayesTraitsV3.0.1-OSX/test/Bio" + str(i+1)
    cmd1 = "mkdir " + inputname
    print cmd1
    os.system(cmd1)
    #outputname="/Users/zhouwenbin/proj/jmodel/Locus" +str(i)
    #if os.path.isfile(inputname) == True:
    #    cmd1 = "java -jar /Users/zhouwenbin/tools/jModelTest-2.1.4/jModelTest.jar -d " + inputname + " -g 4 -i -f -AIC -a -o " + outputname
    #    os.system(cmd1)

