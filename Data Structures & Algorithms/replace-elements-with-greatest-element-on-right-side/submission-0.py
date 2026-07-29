class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        for i in range(length - 1):
            arr[i] = max(arr[i + 1:])
        arr[length - 1] = -1
        return arr