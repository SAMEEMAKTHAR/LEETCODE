class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels=["a","e","i","o","u"]
        a=[]
        b=[]
        for i in s:
            if i in vowels:
                a.append(i)
            else:
                b.append(i)
        count1=Counter(a)
        count2=Counter(b)
        ans1=0
        ans2=0
        if count1:
            ans1=max(count1.values())
        if count2:
            ans2=max(count2.values())
        return ans1+ans2

