from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        index=[i for i in range(len(deck))]
        ans=[-1 for i in range(len(deck))]
        for i in deck:
            idx=index.pop(0)
            ans[idx]=i
            if len(index)>0:
                index.append(index.pop(0))
        return ans