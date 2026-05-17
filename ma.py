import keyboard as kybd
import pyautogui as pyui
import time as tm

running = True
key_1 = input("What should move mouse up?\n")
key_2 = input("What should move mouse down?\n")
key_3 = input("What should move mouse left?\n")
key_4 = input("What should move mouse right?\n")
key_5 = input("What should left click?\n")
key_6 = input("What should right click?\n")
key_7 = input("What should turn on/off keyboard mouse?\n")
block = False

while running:
    if kybd.is_pressed(key_7):
            if not block:
                block = True
                kybd.block_key(key_1)
                kybd.block_key(key_2)
                kybd.block_key(key_3)
                kybd.block_key(key_4)
                kybd.block_key(key_5)
                kybd.block_key(key_6)
                tm.sleep(0.3)
            else:
                block = False
                kybd.unblock_key(key_1)
                kybd.unblock_key(key_2)
                kybd.unblock_key(key_3)
                kybd.unblock_key(key_4)
                kybd.unblock_key(key_5)
                kybd.unblock_key(key_6)
                tm.sleep(0.3)
    if block:
        if kybd.is_pressed(key_1):
            pyui.moveRel(0, -15)
            print("UP!")
        if kybd.is_pressed(key_2):
            pyui.moveRel(0, 15)
            print("DOWN!")
        if kybd.is_pressed(key_3):
            pyui.moveRel(-15, 0)
            print("LEFT!")
        if kybd.is_pressed(key_4):
            pyui.moveRel(15, 0)
            print("RIGHT!")
        if kybd.is_pressed(key_5):
            pyui.leftClick()
            print("LEFT CLICK!")
        if kybd.is_pressed(key_6):
            pyui.rightClick()
            print("RIGHT CLICK!")
