class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        value = {}
        for i in nums:
            if i in value:
                value[i]+=1
            else:
                value[i]=1
        for i in value.keys():
            if value[i]==max(value.values()):
                return(i)