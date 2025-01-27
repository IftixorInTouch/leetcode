class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b, x, y = 0, 0, 0, 0
        num1 = num1.split('+')
        a = int(num1[0])
        b = int(num1[1][:-1])
        num2 = num2.split('+')
        x = int(num2[0])
        y = int(num2[1][:-1])

        real = a * x - b * y
        imaginary = a * y + b * x
        result = f"{real}+{imaginary}i"
        return result


a = Solution()
print(a.complexNumberMultiply("1+-1i", "1+-1i"))
