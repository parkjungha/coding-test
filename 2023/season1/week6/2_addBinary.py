class Solution:
    # Run 56.42% Mem 97.31%
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a,2)
        num2 = int(b,2)
        return format(num1 + num2, 'b')

    # Run 63.17% Mem 62.6%
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i,j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            result.append(str(total % 2)) # 나머지
            carry = total // 2 # 몫

        return ''.join(reversed(result))