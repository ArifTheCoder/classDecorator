
# Solution of question number 1
import re

class Average:
    def __init__(self, munberOfList):
        self.numberOfList = munberOfList

    def average(self):
        sum = 0
        for i in self.numberOfList:
            sum +=i
        averageValue = sum / len(self.numberOfList)
        if averageValue < 6:
            print("Low Average")
        elif averageValue > 6 and averageValue < 12:
            print("Medium Average")
        elif averageValue > 12:
            print("High Average")


listNumber = [5, 7, 12, 15, 9]
mobj = Average(listNumber)
mobj.average()


# Solution of question number 2
class Myclass(object):
    def __init__(self, ln):
        self.ln = ln
        sum = 0
        for i in self.ln:
            sum += i
        averageValue = sum / len(self.ln)

        print(self.ln)

        if averageValue < 6:
            print("Low Average")
        elif averageValue > 6 and averageValue < 12:
            print("Medium Average")
        elif averageValue > 12:
            print("High Average")

    @classmethod
    def getUserValue(cls):
        inputValue = input("Enter a value mixed with letters and number: ")
        extractedNumbers = re.findall(r'\d+', inputValue)
        numbersInInteger = list(map(int, extractedNumbers))
        return cls(numbersInInteger)


clsObj = Myclass.getUserValue()
# question 3