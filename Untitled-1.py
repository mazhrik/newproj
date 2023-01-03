
class LetterFilter:
    def __init__(self,s):
        self.s=s

    def filter_vowels(self):
        try:
            final_result = ""
            vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            

            for i in range(len(self.s)):
                if self.s[i] not in vowel:
                    final_result = final_result + self.s[i]
            return final_result
        except Exception as error:
            return error

    def filter_consants(self):
        try:
            final_result = ""
            consnants=[ 'b','c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z' , 'h', 'r', 'w', 'y']

            for i in range(len(self.s)):
                if self.s[i] not in consnants:
                    final_result = final_result + self.s[i]
            return final_result
        except Exception as error:
            print(error)

obj=LetterFilter('hackerrank')

print('vowels',obj.filter_vowels())
print("consanants",obj.filter_consants())