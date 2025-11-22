class Solution:
    def capitalizeTitle(self, title: str) -> str:
        a=list(title.split())
        ans=[]
        for i in a:
            if len(i)>2:
                ans.append(i.title())
            else:
                ans.append(i.lower())
        return " ".join(ans)

            


            
        