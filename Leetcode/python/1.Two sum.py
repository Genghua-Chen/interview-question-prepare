class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        for i in range(len(nums)-1):

            new_num = nums[i] + nums[i+1]

            if new_num != target:
                continue
                
            else: 
                result.append(i)
                result.append(i+1)
                return result