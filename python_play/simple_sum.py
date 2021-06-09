class Solution:
    def findMaxConsecutiveOnes(self, nums):
        temp_cnt = 0
        max_cnt = 0
        for i in nums:
            if i == 1:
                temp_cnt +=1
            else:
                if temp_cnt > max_cnt:
                    max_cnt = temp_cnt
                temp_cnt = 0
        return temp_cnt if temp_cnt > max_cnt else max_cnt

    def sortSqrtNumbers(self,lst):
        n = len(lst)
        result_lst = [0]*n
        lft_pnt = 0
        right_pnt = len(lst)-1      
        for i in range(n-1,-1,-1):
            if abs(lst[lft_pnt]) > abs(lst[right_pnt]):
                res = lst[lft_pnt]
                lft_pnt +=1
            else:
                res = lst[right_pnt]
                right_pnt -=1
            result_lst[i] = res*res
        return result_lst

    def duplicateZero(self,nums):
        n = len(nums)-1
        curr_pointer = 0
        while curr_pointer <= n:
            if nums[curr_pointer] == 0:
                nums.insert(curr_pointer+1,0)
                nums.pop()
                curr_pointer+=1
            curr_pointer+=1
        return nums

    def mergeSortArray(self, nums1,nums2,m,n):
        '''
        m_only = [1,2,3] nums2 = [2,5,6]
        nums1 = [1,2,3,0,0,0]
        '''
        nums1_only = nums1[:m]
        p1=0
        p2=0
        max_len = m+n
        for p in max_len:
            if ((p1 < m and nums1_only[p1] < nums2[p2]) or p2>=n):
                nums1[p] = nums1_only[p1]
                p1+=1
            else:
                nums1[p] = nums2[p2]
                p2+=1




            
            

    
sol = Solution()
print(sol.mergeSortArray([0],[1],0,1))
#print(sol.duplicateZero([1,0,2,3,0,4,5,0]))
#print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))
#print(sol.sortSqrtNumbers([-4,-1,0,3,10]))
