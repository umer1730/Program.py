class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]   # pick -1 if x < 0 else 1
        rev, x = 0, abs(x)      # reverse starts at 0, take abs of x
        while x:
            x, mod = divmod(x, 10)     # take last digit
            rev = rev * 10 + mod       # build reversed number
            if rev > 2**31 - 1:        # check 32-bit overflow
                return 0
        return sign * rev
sol = Solution()
print(sol.reverse(123))