class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(comb, depth, max_len):
            if depth == max_len:
                answer.append(comb)
                return
                
            for idx in range(max_len):
                if nums[idx] not in comb: 
                    dfs(comb + [nums[idx]], depth + 1, max_len)
                
        answer = []
        
        dfs([], 0, len(nums))
        
        return answer
        