class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        common_indices = []
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
                common_indices.append(i)
        hashmap_guess = {}
        for j in range(len(guess)):
            if j not in common_indices:
                if guess[j] not in hashmap_guess:
                    hashmap_guess[guess[j]]=1
                else:
                    hashmap_guess[guess[j]]+=1
        cows = 0
        for j in range(len(secret)):
            if j not in common_indices:
                if secret[j] in hashmap_guess and hashmap_guess[secret[j]]>0:
                    hashmap_guess[secret[j]]-=1
                    cows+=1

        return f"{bulls}A{cows}B"
