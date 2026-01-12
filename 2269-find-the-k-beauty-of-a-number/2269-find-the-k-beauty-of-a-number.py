class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        a=[int(i) for i in str(num)]
        ans=0
        if len(a)==k:
            return 1
        if k==1:
            i=0
            while i<len(a):
                b=[a[i]]
                key=int("".join(map(str,b)))
                if key!=0 and num%key==0:
                    ans+=1
                    i+=1
                else:
                    i+=1
        elif k>1:
            i=0
            j=i+k-1
            while i<j and j<len(a):
                b=a[i:j+1]
                key=int("".join(map(str,b)))
                if key!=0 and num%key==0:
                    ans+=1
                    i+=1
                    j+=1
                else:
                    i+=1
                    j+=1
        return ans


