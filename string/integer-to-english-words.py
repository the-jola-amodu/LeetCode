class Solution(object):
    def numberToWords(self, num):
        numbers = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }
        def hundredWords(hundred):
            if hundred < 10:
                hundred = "00" + str(hundred)
            elif hundred < 100:
                hundred = "0" + str(hundred)
            else:
                hundred = str(hundred)
            print(hundred)

            result = ""
            if hundred[0] != "0":
                result += numbers[int(hundred[0])] + " Hundred"
            if hundred > 9 and str(hundred)[1] == "1":
                result += " " + numbers[int(hundred[1:])]
                return result
            elif hundred > 9 and str(hundred)[1] != "0":
                result += " " + numbers[int(hundred[1] + "0")]
            if hundred > 99 and str(hundred)[2] != "0":
                result += " " + numbers[int(hundred[2])]
            return result.strip()

        multiples = ["", " Thousand", " Million", " Billion"]
        result = ""
        if 0 <= num <= 20:
            return numbers[num]
        worded = str(num)
        counter = 0
        for i in range(len(worded), 0, -3):
            group = worded[max(i - 3, 0):i]
            new_batch = hundredWords(int(group))
            multiplier = new_batch + multiples[counter] if new_batch else ""
            result = multiplier + " " + result.strip()
            counter += 1
        return result.strip()
        