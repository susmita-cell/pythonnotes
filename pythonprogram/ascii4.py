import sys
print("enter a upper char ")
ch=input()
if len(ch)!=1:
    print("single char allow ")
    sys.exit()
if ch>='A' and ch<='Z':
        x=ord(ch)+32
        print(chr(x))
