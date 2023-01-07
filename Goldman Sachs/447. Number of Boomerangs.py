class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        total_boomerang_possible = 0
        for i in range(len(points)):
            hashmap = {}
            for j in range(len(points)):
                distance = (points[i][0]-points[j][0])*(points[i][0]-points[j][0]) + (points[i][1]-points[j][1])*(points[i][1]-points[j][1])
                if distance not in hashmap:
                    hashmap[distance] = 1
                else:
                    hashmap[distance] += 1
                
            for key in hashmap:
                total_boomerang_possible += hashmap[key]*(hashmap[key]-1)

        return total_boomerang_possible


        
