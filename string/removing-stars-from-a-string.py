class Solution(object):
    def removeStars(self, s):
        result = ''

        for letter in s:
            if letter == '*' and len(result) != 0:
                result = result[:-1]
            else:
                result += letter
        return result