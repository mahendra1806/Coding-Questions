class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value=float('inf')
        max_value=float('-inf')
        max_index_value=-1
        min_index_value=-1
        curr_diff=0

        for i in range(len(arrays)):
            curr_min=arrays[i][0]
            curr_max=arrays[i][-1]
            if i!= max_index_value:
                curr_diff=max(curr_diff,max_value-curr_min)

            if i!=min_index_value:
                curr_diff=max(curr_diff,curr_max-min_value)

                if curr_min < min_value:
                    min_value = curr_min
                    min_index_value = i
        
                if curr_max > max_value:
                    max_value = curr_max
                    max_index_value = i

        return curr_diff


        
