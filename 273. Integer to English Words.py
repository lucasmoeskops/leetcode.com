# Score
#  Runtime: 66%
#  Memory usage: 65%
#
# Description
#
# Convert a non-negative integer num to its English words representation.
#

def single(num):
    if num == 0:
        return 'Zero'
    if num == 1:
        return 'One'
    if num == 2:
        return 'Two'
    if num == 3:
        return 'Three'
    if num == 4:
        return 'Four'
    if num == 5:
        return 'Five'
    if num == 6:
        return 'Six'
    if num == 7:
        return 'Seven'
    if num == 8:
        return 'Eight'
    if num == 9:
        return 'Nine'
    if num == 10:
        return 'Ten'
    if num == 11:
        return 'Eleven'
    if num == 12:
        return 'Twelve'
    if num == 13:
        return 'Thirteen'
    if num == 14:
        return 'Fourteen'
    if num == 15:
        return 'Fifteen'
    if num == 16:
        return 'Sixteen'
    if num == 17:
        return 'Seventeen'
    if num == 18:
        return 'Eighteen'
    if num == 19:
        return 'Nineteen'


def tens(num):
    if num < 30:
        return 'Twenty'
    if num < 40:
        return 'Thirty'
    if num < 50:
        return 'Forty'
    if num < 60:
        return 'Fifty'
    if num < 70:
        return 'Sixty'
    if num < 80:
        return 'Seventy'
    if num < 90:
        return 'Eighty'
    if num < 100:
        return 'Ninety'


WORDS = [
    (100, 10, 'Hundred'),
    (1000, 1000, 'Thousand'),
    (1000000, 1000, 'Million'),
    (1000000000, 1000, 'Billion'),
]


class Solution:
    def numberToWords(self, num: int) -> str:
        if num < 20:
            return single(num)
        if num < 100:
            return tens(num) + (' ' + single(num % 10) if num % 10 else '')
        for amount, limit, word in WORDS:
            if num < amount * limit:
                return (self.numberToWords(num // amount) + ' ' + word + ' ' + self.numberToWords(num % amount)).replace(' Zero', '')
