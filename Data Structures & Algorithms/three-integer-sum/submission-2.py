class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target=0
        nums.sort()
        result=[]
        for start in range(0,len(nums)):
            l=start+1
            r=len(nums)-1
            while l<r:
                if target> (nums[l]+nums[r]+nums[start]):
                    l+=1
                elif target<(nums[l]+nums[r]+nums[start]):
                     r-=1
                else:
                    if  [nums[start],nums[l],nums[r]] not in result:
                         result.append([nums[start],nums[l],nums[r]])
                    l+=1
                    
            
        return result
    