class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        final_result = []
        tmp_inter = [-1, 0]
        for i in range(len(intervals)):
            
            if i == 0:
                final_result.append(intervals[i])
                continue
                
            if final_result[i-1][1] >= intervals[i][0]:
                final_result.append([final_result[i-1][0], intervals[i][1]])
            
            else:
                final_result.append(intervals[i])
                
        return final_result[1:]