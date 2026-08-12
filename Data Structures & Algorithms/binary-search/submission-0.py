class Solution:
    def binarySearch(self,nums:List[int],low:int,high:int,target:int):
        if low >high:
            return -1
        mid=low+(high-low)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
           return self.binarySearch(nums,low,mid-1,target)
        elif nums[mid]<target:
            return self.binarySearch(nums,mid+1,high,target)
        
    def search(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1
        return int(self.binarySearch(nums,low,high,target))
