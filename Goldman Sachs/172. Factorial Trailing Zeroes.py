class Solution:
    def trailingZeroes(self, n: int) -> int:
        denominator = 5
        count =0
        while n>=denominator:
            count += (n//denominator)
            denominator *= 5

        return count
