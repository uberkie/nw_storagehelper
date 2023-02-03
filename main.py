import queue
import threading
import keyboard
import pyttsx3
import openpyxl
import re
import cv2
import numpy
import pytesseract
import mss
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random
import sqlite3





# Fetch the data from the database
# ata = cursor.execute("SELECT * FROM Storage ").fetchall()



class Item:
    def __init__(self):
        self.storage = ""
        self.name = ""
        self.tier = 0  # I, II, III, IV, V
        self.cls = ""  # Epic/Legendary
        self.type = ""  # Amulet/Headgear/...
        self.gs = 0
        self.con = 0
        self.str = 0
        self.dex = 0
        self.int = 0
        self.foc = 0
        self.perks = ""
        self.boe = False
        self.bop = False


storage_commands = {
    '/bs': 'Brimstone Sands',
    '/bm': 'Brimstone Sands',
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
}
cmd = ""
snapshot_queue = queue.Queue()
tts_queue = queue.Queue()
plot_queue = queue.Queue()


pytesseract.pytesseract.tesseract_cmd
current_storage = ""


def str_to_int(str, default):
    try:
        res = int(str)
    except ValueError:
        res = default
    return res


def image_to_text(image):
    return pytesseract.image_to_string(image).strip()


def image_to_number(image):
    str = pytesseract.image_to_string(image, config="--psm 13 -c tessedit_char_whitelist='0123456789'").strip()
    return str_to_int(str, 0)


def alphanum(str):
    str = ''.join([i for i in str if i.isalnum() or i.isspace() or i == "'"])
    return str.strip()


def tts_worker():
    tts = pyttsx3.init()
    tts.setProperty('rate', 150)
    while True:
        text = tts_queue.get()
        if text:
            tts.say(text)
            tts.runAndWait()
        tts_queue.task_done()


def say(text):
    tts_queue.put(text)


def switch_storage(name):
    print("Storage changed to %s" % name)
    global current_storage
    current_storage = name
    say(name)


def snapshot():
    global current_storage
    if not current_storage:
        say("Choose storage first!")
        return
    with mss.mss() as sct:
        img = numpy.array(sct.grab(sct.monitors[1]))
        snapshot_queue.put((current_storage, img))


def on_key_release(e):
    global cmd
    if e.name == '/':
        cmd = '/'
    elif cmd.startswith("/"):
        cmd += e.name
        matching = False
        fullmatch = False
        for c in storage_commands.keys():
            if c.startswith(cmd):
                matching = True
            if c == cmd:
                fullmatch = True
                break
        if fullmatch:
            switch_storage(storage_commands[cmd])
            cmd = ""
        elif not matching:
            cmd = ""

    if e.name == 'insert':
        snapshot()


def apply_brightness_contrast(input_img, brightness=0, contrast=0):
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()
    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)
    return buf


def ocr_worker():
    while True:
        storage, img = snapshot_queue.get()

        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        bright = cv2.cvtColor(apply_brightness_contrast(img, 64, 64), cv2.COLOR_BGR2GRAY)
        bright = cv2.threshold(bright, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        contrast = apply_brightness_contrast(img, 0, 64)
        threshold = 0.
        item_box = [0, 0, 0, 0]
        title_box = [0, 0, 0, 0]
        tier_box = [0, 0, 0, 0]
        type_box = [0, 0, 0, 0]
        gs_box = [0, 0, 0, 0]
        perks_box = [0, 0, 0, 0]
        bind_box = [0, 0, 0, 0]

        gsIcon = cv2.imread('gs.png', 0)
        gsw, gsh = gsIcon.shape[::-1]
        result = cv2.matchTemplate(grayscale, gsIcon, cv2.TM_CCORR_NORMED)  # TM_CCORR_NORMED # TM_SQDIFF
        _, gs_max_val, _, gs_max_loc = cv2.minMaxLoc(result)

        actionsIcon = cv2.imread('actions.png', 0)
        aw, ah = actionsIcon.shape[::-1]
        ares = cv2.matchTemplate(grayscale, actionsIcon, cv2.TM_CCORR_NORMED)
        _, a_max_val, _, a_max_loc = cv2.minMaxLoc(ares)

        tierTxt = cv2.imread('tier.png', 0)
        tw, th = tierTxt.shape[::-1]
        tres = cv2.matchTemplate(grayscale, tierTxt, cv2.TM_CCORR_NORMED)
        _, t_max_val, _, t_max_loc = cv2.minMaxLoc(tres)

        eventItemFrame = cv2.imread('event-item.png', 0)
        ew, eh = eventItemFrame.shape[::-1]
        eres = cv2.matchTemplate(grayscale, eventItemFrame, cv2.TM_CCORR_NORMED)
        _, e_max_val, _, e_max_loc = cv2.minMaxLoc(eres)

        print("gs_max_val = %f" % gs_max_val)
        print("a_max_val = %f" % a_max_val)
        print("t_max_val = %f" % t_max_val)
        if gs_max_val > threshold and a_max_val > threshold and t_max_val > threshold:
            plot_image = None
            item = Item()
            item.storage = storage

            event_name_height = 0
            print(e_max_val)
            if e_max_val > 0.65:
                event_name_height = 41

            item_box[0] = gs_max_loc[0] - 16
            item_box[1] = a_max_loc[1]
            item_box[2] = item_box[0] + 360
            item_box[3] = t_max_loc[1]

            title_box[0] = item_box[0] + 100
            title_box[1] = item_box[1] + 5
            title_box[2] = item_box[2] - 10
            title_box[3] = gs_max_loc[1] - (65 + event_name_height)

            tier_box[0] = title_box[0]
            tier_box[1] = title_box[3]
            tier_box[2] = title_box[2]
            tier_box[3] = tier_box[1] + 22

            type_box[0] = tier_box[0]
            type_box[1] = tier_box[3]
            type_box[2] = tier_box[2]
            type_box[3] = type_box[1] + 22

            gs_box[0] = gs_max_loc[0] + gsw
            gs_box[1] = gs_max_loc[1] - 5
            gs_box[2] = gs_box[0] + 73
            gs_box[3] = gs_box[1] + 45

            perks_box[0] = gs_box[0]
            perks_box[1] = gs_box[1] + 60
            perks_box[2] = item_box[2]
            perks_box[3] = item_box[3] - 30

            bind_box[0] = item_box[0] + 2
            bind_box[1] = item_box[3] - 22
            bind_box[2] = item_box[2] - 2
            bind_box[3] = item_box[3]

            # item_img = grayscale[item_box[1]:item_box[3], item_box[0]:item_box[2]]

            title_img = bright[title_box[1]:title_box[3], title_box[0]:title_box[2]]

            tier_img = contrast[tier_box[1]:tier_box[3], tier_box[0]:tier_box[2]]

            type_img = contrast[type_box[1]:type_box[3], type_box[0]:type_box[2]]

            gs_img = contrast[gs_box[1]:gs_box[3], gs_box[0]:gs_box[2]]

            perks_img = contrast[perks_box[1]:perks_box[3], perks_box[0]:perks_box[2]]

            bind_img = contrast[bind_box[1]:bind_box[3], bind_box[0]:bind_box[2]]

            # if numpy.any(bright):
            #    plot_image = cv2.cvtColor(bright, cv2.COLOR_BGR2RGB)
            #    plot_queue.put((plot_image, None))

            if numpy.any(title_img):
                print(image_to_text(title_img))
                item.name = alphanum(image_to_text(title_img).replace('\r', ' ').replace('\n', ' '))
            if numpy.any(tier_img):
                item.cls = alphanum(image_to_text(tier_img))
                if "legen" in item.cls.lower():
                    item.cls = "Legendary"
                elif "epic" in item.cls.lower():
                    item.cls = "Epic"
                elif "rare" in item.cls.lower():
                    item.cls = "Rare"
                elif "comm" in item.cls.lower():
                    item.cls = "Common"
            if numpy.any(type_img):
                item.type = alphanum(image_to_text(type_img))
            if numpy.any(gs_img):
                item.gs = image_to_number(gs_img)
            if numpy.any(perks_img):
                bullets = image_to_text(perks_img)
                parse_perks(bullets, item)
                parse_stats(bullets, item)
            if numpy.any(bind_img):
                bind = image_to_text(bind_img)
                if "equ" in bind.lower():
                    item.boe = True
                elif "pick" in bind.lower() or "play" in bind.lower():
                    item.bop = True
            item.tier = get_tier(item.gs)
            print(vars(item))
            if store_data(item):
                say('Saved.')
        snapshot_queue.task_done()


def set_border(ws, cell_range):
    thin = openpyxl.styles.Side(border_style="thin", color="000000")
    for row in ws[cell_range]:
        for cell in row:
            cell.border = openpyxl.styles.Border(top=thin, left=thin, right=thin, bottom=thin)


def store_data(item):
    if (not item.name) or (not item.gs) or (not (item.con or item.str or item.dex or item.int or item.foc)) or (
            not item.perks):
        return False
    conn = sqlite3.connect("newworld.db")
    cursor = conn.cursor()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS storage (
            Storage text,
            Type text,
            Tier text,
            Name text,
            Gearscore text,
            CON text,
            STR text,
            DEX text,
            INT text,
            FOC text,
            Perks text,
            BoE text,
            BoP text
        )
    """)
    c.execute("""
        INSERT INTO storage (Storage, Type, Tier, Name, Gearscore, CON, STR, DEX, INT, FOC, Perks, BoE, BoP)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [item.storage, item.type, item.tier, item.name, item.gs, item.con, item.str, item.dex, item.int,
          item.foc, item.perks, 'BoE' if item.boe else '', 'BoP' if item.bop else ''])
    conn.commit()
    conn.close()
    return True

def parse_perks(text, item):
    pattern = "([a-zA-Z ]*):.*"
    res = re.findall(pattern, text)
    if res:
        item.perks = ",".join(res)


def parse_stats(text, item):
    pattern = "[+][ ]?([\d]+)[ ]*([a-zA-Z]+).*"
    res = re.findall(pattern, text)
    for s in res:
        value = str_to_int(s[0], 0)
        type = s[1].strip().lower()
        if value <= 0:
            continue
        if type.startswith("con"):
            item.con = value
        elif type.startswith("str"):
            item.str = value
        elif type.startswith("dex"):
            item.str = value
        elif type.startswith("int"):
            item.int = value
        elif type.startswith("foc"):
            item.foc = value


def get_tier(gearscore):
    if gearscore >= 500:
        return "V"
    elif gearscore >= 400:
        return "IV"
    elif gearscore >= 300:
        return "III"
    elif gearscore >= 200:
        return "II"
    elif gearscore >= 100:
        return "I"
    else:
        return ""


keyboard.on_release(on_key_release)
threading.Thread(target=tts_worker, daemon=True).start()
threading.Thread(target=ocr_worker, daemon=True).start()
# while True:
#    keyboard.read_event()
#    img, rect = plot_queue.get()
#    plt.imshow(img)
#    if rect:
#        plt.gca().add_patch(rect)
#    plt.show()
keyboard.wait()
snapshot_queue.join()
cv2.destroyAllWindows()
