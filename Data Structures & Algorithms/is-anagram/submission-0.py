class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap={}
        for char in s:
            if char not in hashMap:
                hashMap[char]=1
            elif char in hashMap:
                hashMap[char] +=1
        for compareChar in t:
            if compareChar in hashMap and hashMap[compareChar]>0:
                hashMap[compareChar]-=1
            else:
                return False
        return True