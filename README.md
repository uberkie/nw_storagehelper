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

## Demo
[![Video Demo](docs/demo.mp4)]

## What information is saved?

Here is a screenshot from a sample storage file:

![sample-storage](https://user-images.githubusercontent.com/7578087/213796350-d75593f5-7c43-4dd0-b8d1-eb2840733867.png)

