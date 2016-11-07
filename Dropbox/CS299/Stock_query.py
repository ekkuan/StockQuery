import urllib.request
import sys

def highest(date, high):
    length = len(high)
    highest = high[0]
    highDate = date[0]
    for i in range(length):
        if high[i] > highest:
            highest = high[i]
            highDate = date[i]
    return highDate, highest

def lowest(date, low):
    length = len(low)
    lowest = low[0]
    lowDate = date[0]
    for i in range(length):
        if low[i] < lowest:
            lowest = low[i]
            lowDate = date[i]
    return lowDate, lowest

def financeReport():
    page = urllib.request.urlopen("http://chart.yahoo.com/table.csv?s=TGT")
    sys.stdout = open('output.dat', 'w')
    print("Hello")
    pageInfo = page.readline()
    pageInfo = page.readline()
    pageInfo = page.readline()
    pageInfo = page.readline()
    pageInfo = page.readline()
    dateArr = []
    highArr = []
    lowArr = []
    volArr = []
    avgClose = 0

    for each in range(0,5):
        pageInfo = page.readline()
        decodedPageText = pageInfo.decode("utf-8")
        values = decodedPageText.split(",")
        dateArr.append((values[0]))
        highArr.append(float(values[2]))
        lowArr.append(float(values[3]))
        volArr.append(float(values[5]))
        avgClose += float(values[4])
    avgClose = avgClose/5
    highDate, high = highest(dateArr, highArr)
    lowDate, low = lowest(dateArr, lowArr)
    highVolDate, vol = highest(dateArr, volArr)
    print("On", highDate, "share price is $", high, ", the highest of the week.")
    print("On", lowDate, "share price is $", low, ", the lowest of the week.")
    print("Highest trading volume is", vol, "shares, happened on", highVolDate)
    print("This week's average closing price is $", avgClose)

def main():
    financeReport()

if __name__ == "__main__":
    main()
