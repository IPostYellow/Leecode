from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_hash=defaultdict(int)
        paragraph=paragraph.lower()
        flag=(",","."," ","!","?",";","'","")
        left,right=0,0
        while (left<=right) and (right<len(paragraph)):
            if paragraph[right] in flag:
                word=paragraph[left:right]
                if word not in banned:
                    word_hash[word]+=1
                right+=1
                while right<len(paragraph) and paragraph[right] in flag:
                    right+=1
                left=right
            right+=1
        if right>=len(paragraph) and left<len(paragraph):
            word=paragraph[left:right]
            if word not in banned:
                word_hash[word]+=1
        max_word=""
        max_count=0
        for i,v in word_hash.items():
            if v>max_count:
                max_count=v
                max_word=i
        return max_word