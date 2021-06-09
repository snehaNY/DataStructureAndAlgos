def isPalindrom(input):
    table = [0 for _ in range(ord('z') - ord('a')+1)]
    countOdd = 0
    for i in input:
        val = getOrdVal(i)
        if val != -1:
            table[val]+=1
            if table[val]%2:
                countOdd+=1
            else:
                countOdd-=1
    return countOdd<=1

def getOrdVal(ch):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(ch)

    if a<=val<=z:
        return val - a
    elif A<=val<=Z:
        return val - A
    else:
        return -1

if __name__ =="__main__":
    input="Areea aa"
    print("Is {0} a palindrom? :{1}".format(input,isPalindrom(input)))


