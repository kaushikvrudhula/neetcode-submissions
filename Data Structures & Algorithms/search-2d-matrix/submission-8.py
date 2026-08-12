class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        column=len(matrix[0])-1
        for i in range(len(matrix)):
            if matrix[i][column] == target:
                return True
            if matrix[i][column] > target:
                return self.binarySearch(matrix[i],target,0,len(matrix[i])-1)
                break
        return False
            

            
            
    def binarySearch(self, row: List[int], target: int,low:int,high:int):
        
        if low>high:
            return False
        mid=low+(high-low)//2
        if row[mid]==target:
            return True
        if row[mid]>target:
            return self.binarySearch(row,target,low,mid-1)
        elif row[mid]<target:
            return self.binarySearch(row,target,mid+1,high)