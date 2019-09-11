# vocabIT
Simple python code which sends notification of the word and the meaning to your phone.

How to use

`pip install notify-run`

`notify-run register` -  This will show a link or a qr code, use it to register your device where you want your notifications.

`pip install xlrd`

Open `sendVocab.py` and change the timer as per your preference in `time.sleep(yourtime)`.

Now once you're done with all this, just run `python sendVocab.py` or `python3 sendVocab.py` 

ToDO:

`Get a new excel sheet which has sentences as examples too`


`V 2.0`

`Randomized the words and made sure everday a different set of words is sent(40 at a time)`

`Words will be send 40 at a time, and then the same 40 will be sent again and again for revision in the time span`

`It starts at 10 in the morning and ends at around 8:30 evening to make sure even the revision of words is sent how many ever times in that gap, not necesarilly twice`
