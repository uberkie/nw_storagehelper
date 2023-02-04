# nw_storagehelper

This is an early prototype of a storage helper tool for the New World game.
It only works for armor and weapons tier2 or greater

So far works only at 1920x1080 resolution. Will definitely need a rework to be resolution independent.

You need to have tesseract installed in the following directory
'C:\Tesseract-OCR'
You can download it from https://github.com/UB-Mannheim/tesseract/wiki
Also you need to have python installed.

Once that is done you can either use git clone or download the .exe file from the release page

## How to use:

1. Start Anaconda prompt.
2. cd into the directory
  ##Skip step 3 if you downloaded the .exe file
3. Run pip -install -r requirements.txt to install dependencies
4. Run the `main.py` script. Useally the command will be 'python main.py'
5. Start the game
6. While in in-game type into the chat window `/brightwood`, `/bw`, `/everfall`, `/ef` etc, you dont have to press enter. to tell the script what storage      you will be browsing.
7. Point mouse over an item and press `[Insert]` once  key to save that item
8. Wait 1 or 2 seconds you hear "Saved" in your headphones/speakers
9. Results are saved to `newworld.db` file.
10. To browse the saved resaults run the gui app the command will be 'python guiapp.py'

11. In the GUI in the search bar you can seacrh  for any perk/item type/gearscore
12. You can also with 2 condition "freedom+shirking fortify" this will return all items whit those 2 perks where the + is the delimeter
13. You can also "fre+shi for" to search it matches characters not the actuall word.
14. All the columns can be use to filter ascending or descending order
15. To delte a item just select the item and click delete

Store location commands:
```
/bs /bm  = Brimstone Sands
/eb /es  = Ebonscale
/mb /mon = Monarch Buffs
/ck /cu  = Cutlass Keys
/bw /br  = Brightwood
/ef /ev  = Everfall
/eb /ea  = Eastburn
/ww /wi  = Winsward
/fl /fi  = First Light
/wf /we  = Weavers Fen
/rw /ree = Reekwater
/md /mo  = Mourningdale
/rs /res = Restless Shores
/cp /cl  = Cleaves Point
/vh /va  = Valor Hold
/ls /la  = Last Stand
/mr /mh  = Mountainrise
/tm /ta  = Taberna Mercatus
/wa /wi  = Wikala al-Waha
```

## Demo
https://user-images.githubusercontent.com/7578087/214102154-3e4e15ef-1b4c-4923-adb9-d3598f6f98a2.mp4

## What information is saved?

Here is a screenshot from a sample storage file:

![sample-storage](https://user-images.githubusercontent.com/7578087/213796350-d75593f5-7c43-4dd0-b8d1-eb2840733867.png)

The gui displays according to weapon type and perks
## Search for a Void Guantlet
![voidnw](https://user-images.githubusercontent.com/44478849/213962090-616ee1fd-03a0-49dc-b250-440887e3073d.png)

## Search for Fire
![firenw](https://user-images.githubusercontent.com/44478849/213962131-5f48722c-12e8-4748-9b80-8f03943f86dc.png)



