from collections import Counter

def chkPerm(str1,str2):
    if len(str1)!= len(str2):
        return False
    counter = Counter()
    for s in str1:
        counter[s] += 1
    for s in str2:
        if counter[s] == 0:
            return False
        counter[s] -=1
    return True

if __name__ == "__main__":
    input1 = "apple"
    input2 = "pAple"
    if chkPerm(input1,input2):
        print("Strings have same characters")
    else:
        print("Strings are NOT permutation of one another")