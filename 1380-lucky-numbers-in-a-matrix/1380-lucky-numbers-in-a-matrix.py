class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        a=[]
        for i in matrix:
            j=min(i)
            a.append(j)
        key=max(a)
        b=[]
        for i in zip(*matrix):
            b.append(max(i))
        if key in b:
            return [key]
        else:
            return []