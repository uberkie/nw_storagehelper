# nw_storagehelper

This is an early prototype of a storage helper tool for the New World game.

So far works only at 1920x1080 resolution. Will definitely need a rework to be resolution independent.

## How to use:

1. Start Anaconda prompt.
2. cd into the directory
2. Run pip -install -r requirements.txt to install dependencies
3. Run the `main.py` script
4. Start the game
5. While in in-game chat, type `/brightwood`, `/bw`, `/everfall`, `/ef`, etc. to tell the script what storage you will be browsing.
6. Point mouse over an item and press `[Insert]` key to save that item
7. Wait until you hear "Saved" in your headphones/speakers
8. Results are saved to `storage.xlsx` file

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

