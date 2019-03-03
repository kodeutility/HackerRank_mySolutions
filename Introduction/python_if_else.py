# HackerRank        : https://www.hackerrank.com/kodeutility
# GitHub            : https://www.github.com/kodeutility
# Portfolio website : https://kodeutility.github.io/
# Author            : Kiran BG

if __name__ == '__main__':

    N = int(input())

    if N%2!=0:
        print("Weird")
    else:
        if N>=2 and N<=5:
            print("Not Weird")
        elif N>=6 and N<=20:
            print("Weird")
        elif N>20:
            print("Not Weird")
