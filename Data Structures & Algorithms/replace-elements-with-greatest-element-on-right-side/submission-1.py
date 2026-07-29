class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = []
        n = len(arr)
        for i in range(n):
            cur_max = -1
            for j in range(i + 1, n):
                cur_max = max(cur_max, arr[j])
            output.append(cur_max)
        output[n - 1] = -1
        return output