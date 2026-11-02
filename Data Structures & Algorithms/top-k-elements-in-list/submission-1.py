class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        listoflist=[[] for i in range(len(nums)+1)]

        for n in nums:
            hashmap[n]= 1+hashmap.get(n,0)
        for n,c in hashmap.items():
            listoflist[c].append(n)
        
        res=[]
        for i in range(len(listoflist)-1,0,-1):
            for n in listoflist[i]:
                res.append(n)
                if len(res)==k:
                    return res 