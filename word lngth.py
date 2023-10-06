a=input("input sentence")
b=input("type the word to search:")
list0=a.split()
cnt=0
for i in list0:
    if i==b:
        cnt=cnt+1
print("the term",b,"is appeared",cnt,"times in the given sentence")
    
