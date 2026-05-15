class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=int("".join(map(str,digits)))
        a+=1
        b=[]
        for i in str(a):
            b.append(int(i))
        return b
        