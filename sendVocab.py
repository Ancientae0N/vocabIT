from notify_run import Notify
import xlrd
import time
import random
import schedule 
from collections import defaultdict
from datetime import datetime
from datetime import time as ti



def utc2local (utc):
    epoch = time.mktime(utc.timetuple())
    offset = datetime.fromtimestamp (epoch) - datetime.utcfromtimestamp (epoch)
    return utc + offset

def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or utc2local(datetime.utcnow()).time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

location = "Barron.xlsx" #location of excel file
wb = xlrd.open_workbook(location)  #opens the excel file
no_of_sheets = 23
notify = Notify() #used for notification in phones
checkDict = defaultdict(int)
toRepeatList = []

count = 0 # send 40 words only
while(1):
    if(is_time_between(ti(10,00), ti(20,30))): #runs only between 10am to 8:30  pm
        randSheet = random.randint(0,21) 
        print('sheet', randSheet)#gets a random sheet number
        sheet = wb.sheet_by_index(randSheet) 
        randRow = random.randint(2, sheet.nrows-1) #gets a random row number (random word)
        print('row', randRow)
        randText = str(randSheet) + str(randRow) 
        if(count == 40): #done with words for the day, just print again from list
            print("Time for revision now")
            notify.send("Time to revise those 40 words now~~. Will begin in 5 minutes")
            time.sleep(300)
            for i in range(len(toRepeatList)):
                print(toRepeatList[i])
                notify.send(toRepeatList[i])
                time.sleep(300) #5 mins gap

            
        elif(checkDict[randText] == 0): #only send the word if it hasn't been sent
            sheet.cell_value(0, 0) 
            newList = sheet.row_values(randRow)
            toSend = newList[0] + ": " + newList[1]
            toRepeatList.append(toSend)
            print(toSend)
            notify.send(toSend)
            checkDict[randText] +=1 #increment it
            time.sleep(300) #5 minutes gap
            count+=1
        else:
            continue
    else:
        count = 0 # make sure new set of words is sent
        print(count)
print(toRepeatList)
print(checkDict)

#notify.send('Test 1')
