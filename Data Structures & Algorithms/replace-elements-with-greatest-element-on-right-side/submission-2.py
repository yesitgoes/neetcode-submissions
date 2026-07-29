class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        output = [0] * n
        for i in range(n):
            cur_max = -1
            for j in range(i + 1, n):
                cur_max = max(cur_max, arr[j])
            output[i] = cur_max
        return output