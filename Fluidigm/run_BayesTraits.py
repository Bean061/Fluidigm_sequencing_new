import os
path = "/Users/zhouwenbin/tools/BayesTraits/"
path1 = "/Users/zhouwenbin/tools/BayesTraits/test/"
for i in range(20):
    fname1 = path1 + "Nyssa_bio" +str(i+1) + ".txt"
    if os.path.isfile(fname1) == True:

        cmd1 = path + "BayesTraitsV3 " + path1 + "Con_tre2.tre " + path1 + "Nyssa_bio" + str(i+1) + ".txt < " + path1 + "Nyssa_run0.txt"
        print cmd1
        cmd2 = path + "BayesTraitsV3 " + path1 + "Con_tre2.tre " + path1 + "Nyssa_bio" + str(i+1) + ".txt < " + path1 + "Nyssa_run1.txt"

        os.system(cmd1)
        os.system(cmd2)

        cmd3 = "mv " + path1 + "Nyssa_bio" + str(i+1) + ".* " + path1 + "Bio" + str(i+1)
        os.system(cmd3)
