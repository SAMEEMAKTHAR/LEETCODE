class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[]
        s=list(s)
        t=list(t)
        b=list(t)
        for i in s:
            if i in t:
                a.append(i)
                t.remove(i)
        return len(s)==len(a) and len(s)==len(b)