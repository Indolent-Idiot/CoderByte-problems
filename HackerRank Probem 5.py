#Diagonal Difference
#Given a square matrix of size , calculate the absolute difference between the sums of its
#diagonals.
#Input Format
#The first line contains a single integer, . The next lines denote the matrix's rows, with each line
#containing space-separated integers describing the columns.
#Constraints
#Output Format
#Print the absolute difference between the two sums of the matrix's diagonals as a single integer.
#Sample Input
#3
#11 2 4
#4 5 6
#10 8 -12
#Sample Output
#15

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sm1 = 0
    sm2 = 0
    for i in range(n):
        sm1 = sm1 + arr[i][i]
        sm2 = sm2 + arr[i][abs(i - (n - 1))]
    sm = abs(sm2 - sm1)
    return (sm)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
