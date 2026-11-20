class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        res = []

        for i in range(len(nums)):
            complement = target - nums[i]

            if hashmap.get(complement, -1) == -1:
                hashmap[nums[i]] = i
            else:
                res.append(hashmap[complement])
                res.append(i)

        return res

            

        