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

    def get_explanation(self) -> str:
        """

        :return: Возвращает разложение числа в строке вида 'Римкская цифра(или одинаковые цифры) = Арабское число
        (или умножение этого числа на количество одинаковых римский цифр)'
        """
        expl = []

        for roman, count in self.explanation.items():
            expl.append(f'{roman * count} = {count * self.dict_numbers[roman]}')
        return ', '.join(expl)

    def get_char_of_roman_and_index(self, s: str) -> tuple[str, int]:
        """

        :param s: Строка римский цифр, из которой требуется получить арабское число
        :return: char: Римская цифра, с которой начинается строка(1 или 2 символа),
        index: количество символов этой Римской цифры
        """
        char = s[0]
        index = 1
        if len(s) > 1:
            char_tmp = s[0:2]
            if char_tmp in self.dict_numbers:
                char = char_tmp
                index = 2
        return char, index

    def romanToInt(self, s: str) -> int:
        """

        :param s: Строка, из которой требуется получить арабское число
        :return: Арабское число
        """
        prev_char = 'M'
        while s:
            char, index = self.get_char_of_roman_and_index(s)
            if char not in self.dict_numbers:
                return False
            if self.dict_numbers[char] > self.dict_numbers[prev_char]:
                return False
            s = s[index::]
            self.result += self.dict_numbers[char]
            count = self.explanation.get(char, 0) + 1
            self.explanation[char] = count
            prev_char = char
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
