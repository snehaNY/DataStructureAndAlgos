def urlify(inputStr):
    inputStr = inputStr.strip()
    inputStr = inputStr.replace(' ','%20')
    return inputStr

if __name__ == "__main__":
    print(urlify('much ado about nothing      '))