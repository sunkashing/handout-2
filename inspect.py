# import numpy as np

# tmp = np.loadtxt("train.csv", dtype=np.str, delimiter="\t")



from __future__ import print_function
import sys
import math


if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]
    print("The input file is: %s" % (infile))
    print("The output file is: %s" % (outfile))


    fin = open(infile, "r")
    fout = open(outfile, "w")

    lines = fin.readlines()
    revlines = []
    de = 0
    re = 0
    print(lines)

    for x in lines:
        x = x.strip()
        temp = x.split('\t')
        print(temp)
        if temp[2] == 'democrat':
            de += 1
        if temp[2] == 'republican':
            re += 1

    print(de)
    print(re)
    entropy = -((de / (de + re)) * math.log(de / (de + re), 2) + (re / (de + re)) * math.log(re / (de + re), 2))
    error = min(re, de) / (re + de)

    result = 'entropy: ' + str(entropy) + '\n' + 'error: ' + str(error)
    fout.writelines(result)

    fin.close()
    fout.close()