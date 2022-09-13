class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        temp = sorted((x, i) for i, x in enumerate(ratings))
        candies = [1 for i in ratings]
        
        for _, i in temp:
            if i > 0 and ratings[i] > ratings[i - 1]:
                candies[i] = max(candies[i], candies[i - 1] + 1)
            if i < N - 1 and ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)