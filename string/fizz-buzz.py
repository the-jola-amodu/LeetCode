class Solution(object):
    def fizzBuzz(self, n):
        array = []
        for number in range(1, n + 1):
            if number % 3 == 0 and number % 5 == 0:
                array.append("FizzBuzz")
            elif number % 3 == 0:
                array.append("Fizz")
            elif number % 5 == 0:
                array.append("Buzz")
            else:
                array.append(str(number))
        return array