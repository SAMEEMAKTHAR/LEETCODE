class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a=[]
        for i,v in enumerate(list1):
            if v in list2:
                b=list2.index(v)
                a.append((v,i+b))
        
        a=sorted(a,key=lambda x:x[1])
        
        min=a[0][1]
        ans=[]
        for i in a:
            if i[1]==min:
                ans.append(i[0])
        return ans
           
