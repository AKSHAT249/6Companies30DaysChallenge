class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashmap ={}
        minimum_length = len(cards)
        flag = 0
        for i in range(len(cards)):
            if cards[i] not in hashmap:
                hashmap[cards[i]]= i
            else:
                length = i - hashmap[cards[i]] + 1
                hashmap[cards[i]] = i
                if length <= minimum_length:
                    minimum_length = length
                    flag=1
                continue
        if flag==1:
            return minimum_length

        return -1
            
        
