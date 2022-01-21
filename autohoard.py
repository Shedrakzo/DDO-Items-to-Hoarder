import csv
import pyperclip
import pyautogui
import argparse

def hoardform(text, index):
    if index == 0:      #Item name
        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'v')

    if index == 1:      #Item type
        pyperclip.copy(text)
        pyautogui.press('tab', presses = 3)
        if text == "Cosmetic Headwear":
            pyautogui.press('down', presses = 2)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Helm" or text == "Helmet":
            pyautogui.press('down', presses = 2)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Cosmetic Clothing":
            pyautogui.press('down', presses = 5)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Cosmetic Armor":
            pyautogui.press('down', presses = 5)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Cosmetic Quarterstaff  ":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Cosmetic Sceptre":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Medium Armor":
            pyautogui.press('down', presses = 5)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Docent":
            pyautogui.press('down', presses = 5)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Bastard Sword":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Throwing Axe":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Cloak":
            pyautogui.press('down', presses = 6)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Cosmetic Cloak":
            pyautogui.press('down', presses = 6)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Tower shield":
            pyautogui.press('down', presses = 14)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Cosmetic Tower shield":
            pyautogui.press('down', presses = 14)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Necklace":
            pyautogui.press('down', presses = 3)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Buckler shield":
            pyautogui.press('down', presses = 14)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Collar":
            pyautogui.press('down', presses = 17)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Dagger":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Orb":
            pyautogui.press('down', presses = 14)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Boots":
            pyautogui.press('down', presses = 11)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Gloves":
            pyautogui.press('down', presses = 12)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Belt":
            pyautogui.press('down', presses = 8)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Ring":
            pyautogui.press('down', presses = 9)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Battle Axe":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Dart":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Bracers" or text == "Bracer":
            pyautogui.press('down', presses = 7)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Morningstar":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Handwrap":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Club" or text == "Sceptre":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Throwing Hammer":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Scimitar":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Repeating Heavy Crossbow":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Quarterstaff":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Maul":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Dwarven War Axe":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Long Sword":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Light Mace":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Light Crossbow":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Kukri":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Kama":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Heavy Pick":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Great Crossbow":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Falchion":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Large shield":
            pyautogui.press('down', presses = 14)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Light Armor":
            pyautogui.press('down', presses = 5)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Heavy Armor":
            pyautogui.press('down', presses = 5)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Clothing":
            pyautogui.press('down', presses = 5)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Rune Arm":
            pyautogui.press('down', presses = 15)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Goggles":
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Khopesh":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Shuriken":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Great Axe":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Great Sword":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Trinket":
            pyautogui.press('down', presses = 4)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Handaxe":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Short Bow":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Throwing Dagger":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Rapier":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Hand Axe":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Long Bow":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Heavy Crossbow":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Repeating Light Crossbow":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Great Club":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Short Sword":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Warhammer" or text == "War Hammer":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Sickle":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Outfit":
            pyautogui.press('down', presses = 5)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Small shield" or text == "Small Shield":
            pyautogui.press('down', presses = 14)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Light Hammer":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Light Pick":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('down', presses = 1)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        elif text == "Wand":
            pyautogui.press('down', presses = 13)
            pyautogui.press('space')
            pyautogui.press('tab', presses = 2)
            pyautogui.hotkey('ctrl', 'v')
        else:
            pyautogui.press('tab', presses = 2)

    if index == 2:      #Enchantments
        pyperclip.copy(text)
        pyautogui.press('tab', presses = 9)
        pyautogui.hotkey('ctrl', 'v')

    if index == 3:      #Minimum level
        pyperclip.copy(text)
        pyautogui.press('tab', presses = 7)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'v')

    if index == 4:      #Boundness
        pyperclip.copy(text)
        pyautogui.press('tab', presses = 1)
        if text == "":
            pyautogui.press('down', presses = 0)
        elif text == "Bound to Character on Acquire":
            pyautogui.press('down', presses = 1)
        elif text == "Bound to Account on Acquire":
            pyautogui.press('down', presses = 2)
        elif text == "Bound to Character on Equip":
            pyautogui.press('down', presses = 3)
        elif text == "Bound to Account on Equip":
            pyautogui.press('down', presses = 4)
        else:
            pyautogui.press('down', presses = 0)
        pyautogui.press('tab', presses = 5)
        pyautogui.press('enter')


parser = argparse.ArgumentParser()

parser.add_argument('-p', action='store', dest='filepath',
                    help='Sets the file path and/or filename to the CSV file. Note: file extension \'csv\' already included.')

arguments = parser.parse_args()

folder = arguments.filepath

csv_file = csv.reader(open(f"{folder}.csv", 'r'))

pyautogui.hotkey('alt', 'tab') # set focus to Hoarder

for row in csv_file:
    index = 0                   #Iterate the index of the rows to give a spcific action for each
    if index > 4:
        index = 0
    pyautogui.moveTo(439, 36)               #Move mouse to the "Make custom item" button and clicks it to start the process
    pyautogui.click()
    pyautogui.press('tab', presses = 9)
    pyautogui.press('space')                #Clears any data on the form
    pyautogui.press('tab')                  #Goes to the start of the form
    for field in row: 
        hoardform(field, index)
        index += 1




#1 Eyes
#2 Head
#3 Neck
#4 Trinket
#5 Armor
#6 Cloak
#7 Wrists
#8 Waist
#9 Ring
#10 Finger
#11 Feet
#12 Hands
#13 Main Hand
#14 Off Hand
#15 Rune Arm
#16 Quiver
#17 Pet