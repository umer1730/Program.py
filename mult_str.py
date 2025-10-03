class Solution:
    def multiply(self, num1: str, num2: str):
        n3=int(num1)
        n4=int(num2)
        n5=n3*n4
        n6=str(n5)
        return(n6)
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.multiply("123", "456"))