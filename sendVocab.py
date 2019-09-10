from notify_run import Notify
import xlrd
import time
location = "Barron.xlsx" #location of excel file
wb = xlrd.open_workbook(location)  #opens the excel file
sheet = wb.sheet_by_index(0) #gets the sheet number
sheet.cell_value(0, 0) 
notify = Notify() #used for notification in phones
for i in range(1, sheet.nrows):
    newList = sheet.row_values(i)
    toSend = newList[0] + ":" + newList[1]
    notify.send(toSend)
    time.sleep(300)#wait for sometime  (2 mins here) before you send next word with meaning
    notify.send(toSend) #send again for revision
    time.sleep(300)
#notify.send('Test 1')
