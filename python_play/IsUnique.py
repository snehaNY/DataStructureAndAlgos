def isUnique(str):
    if len(str)>128:
        return False
    result = [False for _ in range(128)]
    for s in str:
        val = ord(s)
        if result[val]:
            return False
        else:
            result[val] = True
    return True

if __name__ == "__main__":
    is_unique_str = "abcdefghijkGtr345str"
    if (isUnique(is_unique_str)):
        print("The string has unique characters")
    else:
        print("The string is NOT unique")
    
