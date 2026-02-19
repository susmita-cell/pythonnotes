import sys
print("enter a char ")
ch=input()
if len(ch)!=1:
    print("single char allow ")
    sys.exit()
x=ord(ch)
if x>=65 and x<=90:
    print("upper case")