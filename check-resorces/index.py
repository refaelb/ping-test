import os

os.system('rm resorces.txt')
os.system("kubectl get ns | awk '{print $1}' > ns.txt")
with open("ns.txt") as f:
    ns = f.read().splitlines()
    for i in ns:
        print (i)
        all = 0
        os.system(" kubectl -n {} top pods | grep -v  Running |awk {} > shit/{}.txt".format (i,"'{print $3}'",i))
        with open("shit/{}.txt".format(i)) as f:
            line=f.readlines()
            for j in line:
                if "Mi" in j:
                    s=j.replace("Mi","")
                    num = int(s)
                    sum  = []
                    sum.append(num)
                    for x in sum:
                        all = all + x
        print (i+" use: " + str(all)+" memory")
        with open('resorces.txt','a+') as f:
            f.write("the ns: "+i+" use: " + str(all)+" memory\n")
        os.system("rm shit/{}.txt".format(i))


        os.system(" kubectl -n {} top pods | grep -v  Running |awk {} > shit/{}.txt " .format (i,"'{print $2}'",i))
        with open("shit/{}.txt".format(i)) as f:
            line=f.readlines()
            for j in line:
                if "m" in j:
                    s=j.replace("m","")
                    num = int(s)
                    sum  = []
                    sum.append(num)
                    for x in sum:
                        all = all + x
        print (i+" use: " + str(all)+" cpu")
        with open('resorces.txt','a+') as f:
            f.write("the ns: "+i+" use: " + str(all)+" cpu\n")
        os.system("rm shit/{}.txt".format(i))

                    
        
   