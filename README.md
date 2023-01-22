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
9. Results are saved to `storage.xlsx` file.
10. To browse the saved resaults run the gui app the command will be 'python guiapp.py'

Store location commands storage_commands = {
    '/bs': 'Brimstone Sands',
    '/bm': 'Brimstone Sands',
    '/eb': 'Ebonscale',
    '/es': 'Ebonscale',
    '/mb': 'Monarch Buffs',
    '/mon': 'Monarch Buffs',
    '/ck': 'Cutlass Keys',
    '/cu': 'Cutlass Keys',
    '/bw': 'Brightwood',
    '/br': 'Brightwood',
    '/ef': 'Everfall',
    '/ev': 'Everfall',
    '/eb': 'Eastburn',
    '/ea': 'Eastburn',
    '/ww': 'Winsward',
    '/wi': 'Winsward',
    '/fl': 'First Light',
    '/fi': 'First Light',
    '/wf': 'Weaver''s Fen',
    '/we': 'Weaver''s Fen',
    '/rw': 'Reekwater',
    '/ree': 'Reekwater',
    '/md': 'Mourningdale',
    '/mo': 'Mourningdale',
    '/rs': 'Restless Shores',
    '/res': 'Restless Shores',
    '/cp': 'Cleave''s Point',
    '/cl': 'Cleave''s Point',
    '/vh': 'Valor Hold',
    '/va': 'Valor Hold',
    '/ls': 'Last Stand',
    '/la': 'Last Stand',
    '/mr': 'Mountainrise',
    '/mh': 'Mountainhome',
    '/tm': 'Taberna Mercatus',
    '/ta': 'Taberna Mercatus',
    '/wa': 'Wikala al-Waha',
    '/wi': 'Wikala al-Waha'

## Demo
[![Video Demo](docs/demo.mp4)]

## What information is saved?

Here is a screenshot from a sample storage file:

![sample-storage](https://user-images.githubusercontent.com/7578087/213796350-d75593f5-7c43-4dd0-b8d1-eb2840733867.png)

