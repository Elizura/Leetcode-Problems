class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        a = image[sr][sc]
        def c(image, sr, sc, color):
            if sr >= 0 and sr < len(image) and sc >= 0 and sc < len(image[0]) and image[sr][sc] == a and (sr, sc) not in seen :
                image[sr][sc] = color
                seen.add((sr, sc))
                c(image, sr + 1, sc, color)
                c(image, sr - 1, sc, color)
                c(image, sr, sc + 1, color)
                c(image, sr, sc - 1, color)
            else:
                return
            return image
        return c(image, sr, sc, color)
        
            