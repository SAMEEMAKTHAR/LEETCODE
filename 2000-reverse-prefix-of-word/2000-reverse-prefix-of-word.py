class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            key=word.index(ch)
            first=word[0:key+1]
            first=first[::-1]
            ans=first+word[key+1:]
            return ans
        else:
            return word