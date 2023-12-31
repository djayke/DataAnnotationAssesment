# Here is a python function which will scan input file and extract words that correspond
# to the last value of each row in a staircase. The value are ordered.
#

# Function that initialize dictionary with data read from file
def initDictionary(data):
    file_dict = {}
    for line in data:
        key, value = line.split(' ')
        # add the key, value pair to the dictionary
        file_dict[key] = value.strip("\n")

    return file_dict

# Function to read from file
# Return {data} as content of file
# Return {numRow} as numbers of row in file
def readfile(filename):
    with open(filename, 'r') as fp:
        data = fp.readlines()
        numRow = len(data)

    return numRow, initDictionary(data)


# Return array with index corresponding to staircase row last value
# Return {arr} as array with proper index value in order
def getStaircase(row):
    arr=[]
    step=1
    inc=2
    while step <= row:
        arr.append(step)
        step += inc
        inc += 1

    return arr

# Build a array of word using index and word from given file
# Return {res} an array that contains words corresponding to last index of the staircase
def getWord(Index, Data):
    res = []
    for index in Index:
        res.append(Data[str(index)])

    return res

# Return {strSentence} as a string
def ToString(arr):
    strSentence = ""
    for word in arr:
        strSentence += word + " "
    return strSentence

# decode function
def decode(filename):
    # count rows in file
    rowCount,data = readfile(filename)

    # Build a array representing the staircase index using the number of rows
    arrIndex = getStaircase(rowCount)

    # Build a array of word corresponding to the file word associated with the number
    arrResult = getWord(arrIndex, data)

    # Print result
    print(ToString(arrResult))

if __name__ == '__main__':
    decode("coding_qual.txt")
