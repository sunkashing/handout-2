# import numpy as np

# tmp = np.loadtxt("train.csv", dtype=np.str, delimiter="\t")



from __future__ import print_function
import sys
import math
import numpy as np


if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]
    print("The input file is: %s" % (infile))
    print("The output file is: %s" % (outfile))


    fin = open(infile, "r")
    fout = open(outfile, "w")

    lines = fin.readlines()
    de = 0
    re = 0
    
    lst = []
    for a in lines[1:]:
        lst.append(a.strip().split('\t'))
    nparray = np.array(lst)

    for x in nparray[..., -1]:
        comp = nparray[..., -1][0]
        if x == comp:
            de += 1
        else:
            re += 1

    if re == 0:
        entropy = 0
    else:
        entropy = -((de / (de + re)) * math.log(de / (de + re), 2) + (re / (de + re)) * math.log(re / (de + re), 2))
    error = min(re, de) / (re + de)

    result = 'entropy: ' + str(entropy) + '\n' + 'error: ' + str(error)
    fout.writelines(result)

    fin.close()
    fout.close()