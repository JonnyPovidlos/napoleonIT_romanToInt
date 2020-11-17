class Solution:
    dict_numbers = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    result = 0
    explanation = {}

    def get_explanation(self):
        res = []

        for roman, count in self.explanation.items():
            res.append(f'{roman * count} = {count * self.dict_numbers[roman]}')
        return ', '.join(res)

    def get_char_of_roman_and_index(self, s: str):
        ch = s[0]
        index = 1
        if len(s) > 1:
            ch_tmp = s[0:2]
            if ch_tmp in self.dict_numbers:
                ch = ch_tmp
                index = 2
        return ch, index

    def romanToInt(self, s: str) -> int:
        while s:
            ch, index = self.get_char_of_roman_and_index(s)
            if not ch in self.dict_numbers:
                return False
            s = s[index::]
            self.result += self.dict_numbers[ch]
            count = self.explanation.get(ch, 0) + 1
            self.explanation[ch] = count
        return self.result


solution = Solution()
roman_numbers = input()


res = solution.romanToInt(roman_numbers)
if res:
    print(res)
    if res > 10:
        explanation = solution.get_explanation()
        print(explanation)
else:
    print('Wrong input string')