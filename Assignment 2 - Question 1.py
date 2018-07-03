"""
File: Assignment 2 - Data Structure and Algorithm CSP2348
Question 1: Mini Loto 
"""

#-------------------Insertion Sort

def InsertionSort(lyst):
    i=1                               # starting point to be inserted
    while i<len(lyst):                # Do n-1 insertion
        itemToInsert = lyst[i]  
        j=i-1
        while j>=0:                   # start search 
            if itemToInsert <lyst[j]:
                lyst[j+1] = lyst[j]   #Shift right
                j -= 1
            else:
                break                 # found a index to insert 
        lyst[j+1]= itemToInsert       # insert 
        i += 1

#-------------------Merge Sort

def mergeSort(lyst):
    # lyst            list to be sorted
    # copyBuffer      temporary space needed during merge
    copyBuffer = [None]*(len(lyst))
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst)-1)

def mergeSortHelper(lyst, copyBuffer, low, high):
    # lyst            list to be sorted
    # copyBuffer      temporary space needed during merge
    # high, low      bounds of sublist
    # middle          midpoint of sublist
    if low <high:
        middle = (low+high)//2
        #  print ("low, middle, high = ", low, middle, high)
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle+1, high)
        #    print ("lyst - copyBuffer =>", lyst, "===", copyBuffer)
        merge(lyst, copyBuffer, low, middle, high)

def merge(lyst, copyBuffer, low, middle, high):
    # lyst            list to be sorted
    # copyBuffer      temporary space needed during merge
    # low             beginning of 1st sorted sublist
    # middle          end of 1st sorted sublist
    # middle +1       beginning of 2nd sorted sublist
    # high            end of 2nd sorted sublist

    #initialize i1 and i2 to the 1st items in each sublist
    i1=low
    i2=middle+1

    #interleave  items from the sublists into the
    #copyBuffer in such a way that order is maintained.
    for i in range(low, high+1):
        if i1>middle:
            copyBuffer[i]=lyst[i2] # 1st sublist exhausted
            i2 +=1
        elif i2>high:
            copyBuffer[i] = lyst[i1] # 2nd sublist exhausted
            i1 +=1
        elif lyst[i1]<lyst[i2]:
            copyBuffer[i] = lyst[i1] # item in 1st sublist
            i1 +=1            
        else:                 # lyst[i1]>=lyst[i2]
            copyBuffer[i] = lyst[i2] # item in 2nd sublist  
            i2 +=1
    for i in range(low, high+1):     # copy sorted items back to         
        lyst[i] = copyBuffer[i]      # proer position in lyst

import random

def CommonValue (winNum, gameNum):
    numInCommon = 0
    x1 = x2 = 0
    #print("compare with: ", gameNum)
    while (x1 < len(winNum) and x2 < len(winNum)):
        if(winNum[x1] == gameNum[x2]):
            x1 += 1
            x2 += 1
            numInCommon += 1
        elif(winNum[x1] > gameNum[x2]):
            x2 += 1
        elif(winNum[x1] < gameNum[x2]):
             x1 += 1
    return numInCommon

def winningRepartition (winNum, lotoNum):
    WinTable1 = 0
    WinTable2 = 0
    WinTable3 = 0
    WinTable4 = 0
    for x in range(len(lotoNum)):
       numInCommon = CommonValue(winNum, lotoNum[x])
       if(numInCommon == 6):
           WinTable1 += 1
       elif(numInCommon == 5):
           WinTable2 += 1
       elif(numInCommon == 4):
           WinTable3 += 1
       elif(numInCommon == 3):
           WinTable4 += 1
    WinTable = [WinTable1, WinTable2, WinTable3, WinTable4] 
    return WinTable

def printTable(WinTable):
    one = WinTable[0]
    two = WinTable[1]
    three = WinTable[2]
    four = WinTable[3]
    print("\n|--------------------------------------------|")
    print("| Winner Class | Total number of the winners |")
    print("| 1st Class    |             ", one, "             |")
    print("| 2nd Class    |             ", two, "             |")
    print("| 3rd Class    |             ", three, "             |")
    print("| 4th Class    |             ", four, "            |")
    print("|____________________________________________|\n")

def printMessage(numInCommon):
    if(numInCommon == 6):
        print("You win the game, congratulations!")
    elif(numInCommon == 5):
        print("You are a 2nd class winner, congratulations!")
    elif(numInCommon == 4):
        print("You are a 3rd class winner, congratulations!")
    elif(numInCommon == 3):
        print("You are a 4th class winner, congratulations!")
    else:
        print("Thanks for playing lotto. Good luck next time!")
                

def initialization (size):    
    WinNum = random.sample(range(1,45), 6)
    InsertionSort(WinNum)
    print("WinNum: ", WinNum)
    loto = []
    for count in range(size):
        gameNumbers = random.sample(range(1,45), 6)
        mergeSort(gameNumbers)
        loto.append(gameNumbers)
    allNum = []
    allNum.append(WinNum)
    allNum.append(loto)
    return allNum
 
    
def main ():
    exitProg = 0
    allNum = initialization(1000)
    WinTable = winningRepartition(allNum[0], allNum[1])
    while(exitProg != 1):
        try: 
            choice = int(input("\nIf you want to see the winner statistic table, press 1:\nIf you want to see if you're one of the winner, press 2:\nIf you want to exit, press 3:\nIf you want to draw the numbers again, press 4: \n"))
            if(choice == 1):
                printTable(WinTable)
            elif(choice == 2):
                playerId = int(input("Enter your id number: \n"))
                winNum = allNum[0]
                playerNum = allNum[1][playerId - 1]
                numInCommon = CommonValue(winNum, playerNum)
                print("<Player’s ID: ",playerId,">, <Game-numbers in sequence in lotto: ", playerNum,">;")
                printMessage(numInCommon)
            elif(choice == 3):
                exitProg = 1
            elif(choice == 4):
                main()
        except BaseException:
            print("Please enter a number between 1 and 4")

if __name__ == "__main__":
    main()
