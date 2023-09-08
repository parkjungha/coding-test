class Solution:
    # Run 55.84% Mem 6.48%

    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for digit in digits:
            s += str(digit)
        
        answer = []
        for char in str(int(s)+1):
            answer.append(int(char))
        return answer