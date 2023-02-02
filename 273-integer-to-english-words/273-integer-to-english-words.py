class Solution:
    
    def __init__(self):
        self.ONE_DIGIT = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        
        self.LESS_THAN_20 = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        
        self.FIRST_DIGIT_LESS_THAN_99 = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        
    def three_digits_to_str(self, num:int):
        hundred = num //100
        less_than_hundred = num - hundred * 100
        
        if hundred and less_than_hundred:
            return self.ONE_DIGIT[hundred] + " Hundred " + self.two_digits_int_to_str(less_than_hundred)
        elif not hundred and less_than_hundred:
            return self.two_digits_int_to_str(less_than_hundred)
        elif hundred and not less_than_hundred:
            return self.ONE_DIGIT[hundred] + " Hundred"
        
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        less_than_thousand = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
        result = ""
        if billion:
            result = self.three_digits_to_str(billion) + " Billion "
        if million:
            result += self.three_digits_to_str(million) + " Million "
        if thousand:
            result += self.three_digits_to_str(thousand) + " Thousand "
        if less_than_thousand:
            result += self.three_digits_to_str(less_than_thousand)
        return result.strip()
            
    def two_digits_int_to_str(self, num:int) -> str:
        # This returns empty if num is 0
        if not num:
            return ""
        elif num < 10:
            return self.ONE_DIGIT[num]   
        elif num < 20:
            return self.LESS_THAN_20[num]
        else:
            first_digit = num//10
            second_digit = num%10
            if second_digit:
                return self.FIRST_DIGIT_LESS_THAN_99[first_digit] + " " + self.ONE_DIGIT[second_digit]
            else:
                return self.FIRST_DIGIT_LESS_THAN_99[first_digit]