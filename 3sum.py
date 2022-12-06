from typing import List 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if min(nums)>0:
            return []
        ans =[]
        sorted_list = sorted(nums)
        for i in range(len(sorted_list)):
            if i > 0 and sorted_list[i] == sorted_list[i-1]:
                continue
            one = i
            two = i+1
            three = len(sorted_list)-1
            while two<three:
                suM = sorted_list[one] + sorted_list[two] + sorted_list[three]
                if  suM == 0:
                    ans.append((sorted_list[one] ,sorted_list[two] , sorted_list[three]))
                    two += 1
                    three -= 1
                elif suM < 0:
                    two += 1
                else:
                    three -= 1
                
        return list(set(ans))

print(Solution().threeSum([-2,0,0,2,2]))

