class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix1=set()
        for num1 in arr1:
            while num1:
                prefix1.add(num1)
                num1//=10
        ans=0
        for num2 in arr2:
            while num2:
                if num2 in prefix1:
                    break
                num2//=10
            if num2:
                ans=max(ans,len(str(num2)))
        return ans

        
