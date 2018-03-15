# open the file and store the hex into integer list
def openFile():
    hex_array = []
    with open(filename, 'rb') as f:
        block = f.read()
        print(block)
        for i in block:
            hex_array.append(i)
        return hex_array

# write the modified list back to the file
def writeFile():
    fileByteArray = bytearray(binary_values) # turn the integer list back into a byte array
    # print(fileByteArray)
    with open(filename, 'wb') as f:
        f.write(fileByteArray) # write the byte array back

# change values that occupy 2 hex offsets
def changeTwoPositions(position1, position2, value):
    hex_num = hex(int(value))
    # print(hex_num)
    if len(hex_num) <= 4:
        big = 0
        small = hex_num
        # print(big, " ", small)
        binary_values[position2] = big
        binary_values[position1] = int(small, 16)
    elif len(hex_num) == 5:
        big = hex_num[2:3]
        small = hex_num[3:]
        # print(big, " 5- ", small)
        binary_values[position2] = int(big, 16)
        binary_values[position1] = int(small, 16)
    else :
        big = hex_num[2:4]
        small = hex_num[4:]
        # print(big, " else- " , small)
        binary_values[position2] = int(big, 16)
        binary_values[position1] = int(small, 16)

# change values that occupy only one hex offset
def changeOnePosition(position, value):
    hex_num = hex(int(value))
    # print(hex_num)
    # if len(hex_num) == 3:
    small = hex_num[2:]
    # print(small)
    binary_values[position] = int(small, 16)

# change stats for all characters from 000 - 1FF
def changeCharacterStats():
    next_charactor_position = 32 # the position apart from each other
    HP_p1, HP_p2 = 18, 19 # HP offsets
    MHP_p1, MHP_p2 = 20, 21 # max hp offsets
    Strength_p = 14 # strength offsets
    Int_p = 16 # int offsets
    Dex_p = 15 # dex offsets
    Exp_p1, Exp_p2 = 22, 23 # exp offsets

    # prints out all the character names
    for i in range(len(characterList)):
        print(i, ". ", characterList[i])
    while(True):
        choice = input("Enter the character that you want to change. (0-15) Enter n to quit. ")
        if choice == 'n': return # quit the loop when user wants to quit

        # find the location of the character's stats
        character_offset = next_charactor_position * int(choice)

        print("Stats of :", characterList[int(choice)])
        HP = input("Enter the amount of HP (1-999) ")
        MHP = input("Enter the amount of Max HP (1-999) ")
        Strength = input("Enter the amount of strength (1-99) ")
        Int = input("Enter amount of Int (1-99) ")
        Dex = input("Enter amount of Dex (1-99) ")
        Exp = input("Enter Exp amount (1-9999) ")

        # change HP value
        HP_p2 = HP_p2 + character_offset
        HP_p1 = HP_p1 + character_offset
        changeTwoPositions(HP_p1, HP_p2, HP)

        # change MHP value
        MHP_p2 = MHP_p2 + character_offset
        MHP_p1 = MHP_p1 + character_offset
        changeTwoPositions(MHP_p1, MHP_p2, MHP)

        # change exp values
        Exp_p2 = Exp_p2 + character_offset
        Exp_p1 = Exp_p1 + character_offset
        changeTwoPositions(Exp_p1, Exp_p2, Exp)
        # change strength value
        Strength_p += character_offset
        changeOnePosition(Strength_p, Strength)

        # change int value
        Int_p += character_offset
        changeOnePosition(Int_p, Int)

        # change dex value
        Dex_p += character_offset
        changeOnePosition(Dex_p, Dex)

# change item values in game
def changeItemsValue():
    Gold = input("Enter the amount of Gold (100-9999) ")
    Keys = input("Enter the amount of Keys (1-99) ")
    BlackBadge = input("Enter the 1 for BlackBadge, 0 for none ")
    Magic_Carpet = input("Enter the number of magic carpets (1-100) ")
    Magic_axes = input("Enter the number of magic axes (1-100) ")
    Skull_Keys = input("Enter the number of Skull keys (1-100) ")

    Gold_p1, Gold_p2 = 516, 517 # gold value offsets
    Keys_p = 518 # keys offset
    BlackBadge_p = 536 # blackbadge offset
    Skull_Keys_p = 523 # skull keys offset
    Magic_axes_p = 576 # magic axes offset
    Magic_Carpet_p = 522 # magic carpet offset

    # change gold value
    changeTwoPositions(Gold_p1, Gold_p2, Gold)
    # change key values
    changeOnePosition(Keys_p, Keys)
    # Enable blackbadege
    if BlackBadge == "1": changeOnePosition(BlackBadge_p, 255)
    else: changeOnePosition(BlackBadge_p, 0)
    # change magic carpet value
    changeOnePosition(Magic_Carpet_p, Magic_Carpet)
    # change Magic axe value
    changeOnePosition(Magic_axes_p, Magic_axes)
    # change skull key value
    changeOnePosition(Skull_Keys_p, Skull_Keys)

# the list of characters
characterList = ['Myself', 'Shamino', 'Iolo', 'Mariah', 'Geoffrey', 'Jaana', 'Julia', 'Dupre', 'Katrina', 'Sentri', 'Gwenno', 'Johne', 'Gorn', 'Maxwell', 'Toshi', 'Saduj']

filename = 'Ultima_5\saved.gam' # file name
binary_values = openFile() # open the file and read in the binary
# print(binary_values)

# change the characters stats
changeCharacterStats()
changeItemsValue()

# write the result back to the file
writeFile()
