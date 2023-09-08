class Solution:
    # Runtime 40.59% Memory 97.92%
    def intToRoman(self, num: int) -> str:
        dic = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        answer = ''
        for k, v in dic.items():
            answer += k * (num // v)
            if num // v != 0:
                num -= (num // v) * v

        return answer 