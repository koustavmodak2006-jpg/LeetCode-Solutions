class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a = [nums[0]]
        b = [nums[1]]
        i = 2
        while i <= len(nums) -1:
            if a[-1] > b[-1]:
                a.append(nums[i])
            else:
                b.append(nums[i])
            i+=1
        return a+b