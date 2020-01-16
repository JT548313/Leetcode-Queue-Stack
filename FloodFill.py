from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited= []
        def helper(sr, sc, cur_color):

            if (sr,sc) in visited:
                return
            elif 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] == cur_color:
                image[sr][sc] = newColor
                visited.append((sr,sc))
            else:
                return

            helper(sr + 1, sc, cur_color)
            helper(sr - 1, sc, cur_color)
            helper(sr, sc + 1, cur_color)
            helper(sr, sc - 1, cur_color)

        cur_color = image[sr][sc]

        if cur_color == newColor:
            return image
        else:
            helper(sr, sc, cur_color)

        return image

image = [[1,1,1],[1,1,0],[1,0,1]]
s = Solution()
print(s.floodFill(image, 1, 1, 2))
