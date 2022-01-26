import sys   # Command-line arguments
import re    # Regular expression tools
import os    # Checking if file exists

# Set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

inputFile = sys.argv[1]
outputFile = sys.argv[2]

# Asserts that input file exists
if not os.path.exists(inputFile):
    print("text file input %s doesn't exist! Exiting" % inputFile)
    exit()

# Opens input file and counts the words using a dictionary
wordDict = {}
with open(inputFile, 'r') as file:
    for line in file:
        for word in re.findall(r"[\w]+", line):
            word = word.lower()
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict[word] = 1

# Writes the sorted words with numbers of instances in text
# in the output file
with open(outputFile, 'w') as resFile:
    for key in sorted(wordDict.keys()):
        resFile.write(key + ' ' + str(wordDict[key]) + '\n')
