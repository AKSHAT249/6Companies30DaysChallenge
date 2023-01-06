class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(a,b):
            return ((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]))

        d12 = distance(p1,p2)
        d13 = distance(p1,p3)
        d14 = distance(p1,p4)
        d23 = distance(p2,p3)
        d24 = distance(p2,p4)
        d34 = distance(p3,p4)

        liste = [d12 , d13 , d14 , d23 ,d24 , d34]

        if 0 in liste:
            return False

        hashmap = {}
        for key in liste:
            if key not in hashmap:
                hashmap[key] = 1
            else:
                hashmap[key]+=1
        print(hashmap)
        answer = []
        for key in hashmap:
            answer.append(hashmap[key])

        if (answer[0]==2 and answer[1]==4)or(answer[0]==4 and answer[1]==2):
            return True
        else:
            return False
