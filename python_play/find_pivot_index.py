def find_pivot_index(lst):
    lt_sum = sum(lst)
    left_sum = 0
    for idx, num in enumerate(lst):
        if (left_sum == lt_sum - left_sum - num):
            return idx
        left_sum += num
    return -1

def largest_integer(input):
    if len(input) == 1:
        return 1
    lst = []
    for idx, num in enumerate(input):
        lst.append((num,idx))
    lst.sort(key=lambda x:x[0],reverse = True)
    if (lst[0][0]//2 >= lst[1][0]):
        return lst[0][1]
    else:
        return -1

'''def plusOne(digits):
    if len(digits) == 0:
        return [digits[0]+1]
    lst = []
    digit_plus_one = [chr for chr in str(int(''.join([str(num)for num in digits]))+1)]
    return digit_plus_one'''

def plusOne(digits):
        n = len(digits)

        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                # and the job is done
                return digits

        # we're here because all the digits are nines
        return [1] + digits

print(plusOne([9,8,9]))
#print(largest_integer([1,2,3,4]))

#print(find_pivot_index([1,7,3,6,5,6]))
#print(find_pivot_index([1,2,3]))
#print(find_pivot_index([2,1,-1]))
