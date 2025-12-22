class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        a=0
        for i in range(len(arr1)):
            b=0
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])>d:
                    b+=1
            if len(arr2)==b:
                a+=1
        return a


        