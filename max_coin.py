def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        max_coin=0
        l=1
        r=len(piles)-1
        i=0
        while i<len(piles) and l<r:
            max_coin+=piles[l]
            l+=2
            r-=1
            i+=1
        return max_coin
