from typing import List

class LargestTriangleArea:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxarea = 0        
        for i in range(len(points)):
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                for k in range(j + 1, len(points)):
                    p3 = points[k]
                    area = 0.5 * abs(
                        p1[0] * (p2[1] - p3[1]) + 
                        p2[0] * (p3[1] - p1[1]) + 
                        p3[0] * (p1[1] - p2[1])
                    )
                    
                    maxarea = max(maxarea, area)

        return maxarea