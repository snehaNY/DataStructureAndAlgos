from collections import Counter

def strCompress(input):
    if len(input) <= 2:
        return input
    cntr = Counter()
    output = ''
    for i in input:
        cntr[i] +=1
    for key,val in cntr.items():
        output += key+str(val)
    return min(input,output,key=len)        

if __name__ =="__main__":
    input = 'abcd'
    print("The compressed form of {0} is {1}".format(input,strCompress(input)))


