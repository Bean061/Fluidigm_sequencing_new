import os
path = "/Users/zhouwenbin/tools/BayesTraits/"
path1 = "/Users/zhouwenbin/tools/BayesTraits/test_conti/"

filename1 = "/Users/zhouwenbin/tools/BayesTraits/test_conti/output.txt"
for i in range(19):
    fname1 = path1 + "Bioclim17_" +str(i+2) + ".txt"
    if os.path.isfile(fname1) == True:

        cmd1 = path + "BayesTraitsV3 " + path1 + "species.trees " + path1 + "Bioclim17_" + str(i+2) + ".txt < " + path1 + "run0.txt"
        print cmd1
        os.system(cmd1)


        filename = "/Users/zhouwenbin/tools/BayesTraits/test_conti/Bioclim17_" + str(i+2) + ".txt.Stones.txt"
        f1 = open(filename, 'r')  # open the the .tre file.
        s = len(f1.readlines())
        f1.close()
        f1 = open(filename, 'r')
        lines = f1.readlines()
        sum = lines[int(s - 1)]
        f2 = open(filename1, 'a')
        f2.write(sum)
        f2.close()
        f1.close()

        cmd2 = path + "BayesTraitsV3 " + path1 + "species.trees " + path1 + "Bioclim17_" + str(i+2) + ".txt < " + path1 + "run1.txt"
        os.system(cmd2)
        filename = "/Users/zhouwenbin/tools/BayesTraits/test_conti/Bioclim17_" + str(i+2) + ".txt.Stones.txt"
        f1 = open(filename, 'r')  # open the the .tre file.
        s = len(f1.readlines())
        f1.close()
        f1 = open(filename, 'r')
        lines = f1.readlines()
        sum = lines[int(s - 1)]
        f2 = open(filename1, 'a')
        f2.write(sum)
        f2.close()
        f1.close()

        #cmd3 = "mv " + path1 + "Nyssa_bio" + str(i+1) + ".* " + path1 + "Bio" + str(i+1)
        #os.system(cmd3)
