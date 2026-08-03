class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        sortedStrings = ["".join(sorted(string)) for string in strs]
        for index in range(0,len(sortedStrings)):
                dic.setdefault(sortedStrings[index],[]).append(strs[index])
        return list(dic.values()) 
