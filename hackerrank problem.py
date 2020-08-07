#John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

#For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

#Function Description

#Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

#sockMerchant has the following parameter(s):

#n: the number of socks in the pile
#ar: the colors of each sock
#Output Format

#Return the total number of matching pairs of socks that John can sell.

#Sample Input

#9
#10 20 20 10 10 30 50 10 20
#Sample Output

#3



import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dct = dict()
    pairs = 0
    for i in range(len(ar)):
        dct[ar[i]] = dct.get(ar[i], 0) + 1

    for values, counts in dct.items():
        print(counts)
        pairs = pairs + int(counts / 2)
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
