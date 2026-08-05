class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            j = i+1
            k = j+1

            while j <=len(nums)-1 and k <=len(nums)-1:
                if nums[k] == nums[j] == nums[i] and i!=j and j!=k:
                    if res == 0:
                        res = max(0,abs(i-j) + abs(j-k) + abs(i-k))
                    res = min(res,abs(i-j) + abs(j-k) + abs(i-k))
                    break

                if nums[j] != nums[i]:
                    j+=1
                if nums[k] != nums[i] or j==k:
                    k+=1

        return res if res!=0 else -1