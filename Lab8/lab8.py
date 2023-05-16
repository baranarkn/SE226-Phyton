from abc import ABC

#Question 1
class FileReceiver(ABC):
    address = ""

    def __init__(self, address):
        self.address = address

    def calculateFreqs(self):
        pass


#Question 2-3
class ListCount(FileReceiver):
    def calculateFreqs(self):
        frequency_list = []

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char != " ":
                        isFound = False
                        for pairs in frequency_list:
                            if pairs[0] == char:
                                pairs[1] += 1
                                isFound = True
                                break
                        if not isFound:
                            frequency_list.append([char, 1])

        for pairs in frequency_list:
            print("List ->", pairs[0], "\tResulting List ->", pairs[0], "=", pairs[1])


#Question 2-4
class DictCount(FileReceiver):
    def calculateFreqs(self):
        frequency_dict = {}

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char != " ":
                        if char in frequency_dict:
                            frequency_dict[char] += 1
                        else:
                            frequency_dict[char] = 1

        for key, value in frequency_dict.items():
            print("Dict ->", key, "0 \tUpdated Dict ->", key, value)


#Question 5
listCounter = ListCount("weirdWords.txt")
listCounter.calculateFreqs()
print("\n\n")
dictCounter = DictCount("weirdWords.txt")
dictCounter.calculateFreqs()