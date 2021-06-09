A = [-1,3,8,2,9,5]
B = [4,1,2,10,5,20]

def sum_to_nearest(lst1, lst2,target):
    result = [[(i,j),abs(target-(i+j))] for i in A for j in B]
    small_diff = lambda result:result[1]
    result.sort(key = small_diff)
    print(result)
    print("The closest pair is ",result[0][0])
#sum_to_nearest(A,B,24)

def closest_sum_pair(lst1, lst2, target):
    sort_lst1 = sorted(lst1)
    sort_lst2 = sorted(lst2)
    smallest_diff = abs(sort_lst1[0]+sort_lst2[0] - target)
    closest_pair = (sort_lst1[0],sort_lst2[0])
    i = 0
    j = len(lst2) - 1
    while (i < len(lst1) and j >=0):
        curr_diff = (sort_lst1[i] + sort_lst2[j]) - target
        if (abs(curr_diff) < smallest_diff):
            smallest_diff = abs(curr_diff)
            closest_pair = (sort_lst1[i] , sort_lst2[j])
        if curr_diff == 0:
            return closest_pair
        if curr_diff < 0:
            i+=1
        else:
            j-=1
    return closest_pair

        



print(closest_sum_pair(A,B,target=24))
    




