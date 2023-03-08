# Score
#  Runtime: 8%
#  Memory usage: 5%
#
# Description
#
# You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:
#
#    Choose 2 distinct names from ideas, call them ideaA and ideaB.
#    Swap the first letters of ideaA and ideaB with each other.
#    If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
#    Otherwise, it is not a valid name.
#
# Return the number of distinct valid names for the company.
#

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ending_to_letter = defaultdict(set)
        letter_to_ending = defaultdict(int)
        letter_to_other_letter = defaultdict(Counter)
        total = 0
        
        for idea in ideas:
            for l in ending_to_letter[idea[1:]]:
                letter_to_other_letter[idea[0]][l] += 1
                
            ending_to_letter[idea[1:]].add(idea[0])
            letter_to_ending[idea[0]] += 1
            
        for idea in ideas:
            start, ending = idea[0], idea[1:]
            
            for letter in set(letter_to_ending) - ending_to_letter[ending]:
                total += letter_to_ending[letter] - letter_to_other_letter[letter][idea[0]] - letter_to_other_letter[idea[0]][letter]
                
        return total
