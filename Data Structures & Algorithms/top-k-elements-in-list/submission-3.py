class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        result=[]
        for num in nums:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
        dic=dict(sorted(dic.items(), key=lambda x: x[1],reverse=True))
        for value in dic.keys():
            if k!=0:
                result.append(value)
                k-=1
        return result
                