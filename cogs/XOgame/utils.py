import numpy as np
from cogs.XOgame.constants import *
import os

class TicTacToe():
    def __init__(self,player1,player2,emptybox = "☐",x = "❌",o = "⚪"):
        self.player1 = player1
        self.player2 = player2
        self.emptybox = emptybox
        self.x = x
        self.o = o

    def create_grid(self):
        grid = np.zeros((3,3))
        return grid

    def delete_grid(self):
        try:
          os.remove("gridfile.npy")
        except:
            pass

    def new_grid(self):
        self.delete_grid()
        grid = self.create_grid()
        np.save("gridfile",grid)
        

    def fill_x(self,position):
        if position == 1:
            position = one
        if position == 2:
            position = two
        if position == 3:
            position = three
        if position == 4:
            position = four
        if position == 5:
            position = five
        if position == 6:
            position = six
        if position == 7:
            position = seven
        if position == 8:
            position = eight
        if position == 9:
            position = nine
        try:
            np.load("gridfile.npy")
        except FileNotFoundError:
            print("grid not found .... creating new one")
            grid = self.create_grid()
            np.save("gridfile",grid)

        grid = np.load("gridfile.npy")
        if grid[position] == 0:
            grid[position] = 1
        else:
            raise Exception("That box has already been filled")


        np.save("gridfile",grid)

        return grid

    def fill_o(self,position):
        if position == 1:
            position = one
        if position == 2:
            position = two
        if position == 3:
            position = three
        if position == 4:
            position = four
        if position == 5:
            position = five
        if position == 6:
            position = six
        if position == 7:
            position = seven
        if position == 8:
            position = eight
        if position == 9:
            position = nine
        try:
            np.load("gridfile.npy")
        except FileNotFoundError:
            print("grid not found .... creating new one")
            grid = self.create_grid()
            np.save("gridfile",grid)

        grid = np.load("gridfile.npy")

        if grid[position] == 0:
            grid[position] = 2
        else:
            raise Exception("That box has already been filled")







        np.save("gridfile",grid)

        return grid

    def clean_rows(self,row1,row2,row3):
        cleanedrow1 = ""
        cleanedrow2 = ""
        cleanedrow3 = ""
        m = 0
        n = 0
        p = 0
        for i in row1:
                if i == 0:
                    index = np.where(row1 == i)
                    if m == 0:
                        cleanedrow1 += "1️⃣"

                    elif m == 1:
                        cleanedrow1 += "2️⃣"

                    elif m == 2:
                        cleanedrow1 += "3️⃣"


                if i == 1:
                    cleanedrow1 += self.x
                if i == 2:
                    cleanedrow1 += self.o

                m += 1

        for i in row2:

            if i == 0:
                index = np.where(row2 == i)
                if n == 0:
                    cleanedrow2 += "4️⃣"

                elif n == 1:
                    cleanedrow2 += "5️⃣"

                elif n == 2:
                    cleanedrow2 += "6️⃣"



            if i == 1:
                cleanedrow2 += self.x
            if i == 2:
                cleanedrow2 += self.o

            n += 1

        for i in row3:
            if i == 0:
                index = np.where(row3 == i)
                if p == 0:
                    cleanedrow3 += "7️⃣"

                elif p == 1:
                    cleanedrow3 += "8️⃣"

                elif p == 2:
                    cleanedrow3 += "9️⃣"
            if i == 1:
                cleanedrow3 += self.x
            if i == 2:
                cleanedrow3 += self.o

            p += 1

        cleanedrows = f"{cleanedrow1}\n{cleanedrow2}\n{cleanedrow3}"
        return cleanedrows

    def ended(self):
        grid = np.load("gridfile.npy")
        check = 0

        for row in grid:
            for i in row:
                if i != 0:
                    check += 1
                else:
                    pass

        if check == 9:
            #print("check",check)
            return True
        if check < 9:
            #print("check", check)
            return False


    def row_completed(self,grid):

        result_list = []

        for row in grid:
            if 0 not in row:
                if row[0] == row[1]:
                    if row[1] == row[2]:
                        result_list.append(True)
                    else:
                        result_list.append(False)
                else:
                    result_list.append(False)
            else:
                result_list.append(False)

        if True in result_list:
            print('row completed')
            return True
        else:
            return False
            print("row not completed")


    def column_completed(self,grid):

        result_list = []

        for row in grid.transpose():
            if 0 not in row:
                if row[0] == row[1]:
                    if row[1] == row[2]:
                        result_list.append(True)
                    else:
                        result_list.append(False)
                else:
                    result_list.append(False)
            else:
                result_list.append(False)

        if True in result_list:
            return True
        else:
            return False

    def diagonal_completed(self,grid):

        diag1 = np.diagonal(grid)
        diag2 = np.diagonal(np.rot90(grid))

        result_list = []
        if 0 not in diag1:
            if diag1[0] == diag1[1]:
                if diag1[1] == diag1[2]:
                    result_list.append(True)
                else:
                    result_list.append(False)
            else:
                result_list.append(False)
        if 0 not in diag2:
            if diag2[0] == diag2[1]:
                if diag2[1] == diag2[2]:
                    result_list.append(True)
                else:
                    result_list.append(False)
            else:
                result_list.append(False)
        else:
            result_list.append(False)


        if True in result_list:
            return True
        else:
            return False


    def is_won(self):
        grid = np.load("gridfile.npy")

        if self.row_completed(grid):
            return True
        elif self.column_completed(grid):
            return True
        elif self.diagonal_completed(grid):
            return True
        else:
            return False

    def show_array(self):
        try:
            grid = np.load("gridfile.npy")
            return grid
        except:
            pass

    def empty_boxes(self):

        try:
            grid = np.load("gridfile.npy")
            index_list = np.where(grid.flatten() == 0.)
            final_val = ""

            for i in index_list[0]:
                i += 1
                print(i)
                final_val += str(i)

            return final_val

        except:
            pass







    def show_grid(self):
        try:
            np.load("gridfile.npy")
        except FileNotFoundError:
            grid = self.create_grid()
            np.save("gridfile",grid)

        grid = np.load("gridfile.npy")

        row1 = grid[0,:]
        row2 = grid[1,:]
        row3 = grid[2,:]


        cleanedrows = self.clean_rows(row1,row2,row3)

        return cleanedrows

def deleteGame():
    try:
       os.remove("gridfile.npy")
    except:
        pass

def toEmoji(nums_str):
    emojiList  = []
    for i in nums_str:
        if i == "1":
            emojiList.append("1️⃣")
        if i == "2":
            emojiList.append("2️⃣")
        if i == "3":
            emojiList.append("3️⃣")
        if i == "4":
            emojiList.append("4️⃣")

        if i == "5":
            emojiList.append("5️⃣")

        if i == "6":
            emojiList.append("6️⃣")
            
        if i == "7":
            emojiList.append("7️⃣")

        if i == "8":
            emojiList.append("8️⃣")

        if i =="9":
            emojiList.append("9️⃣")

    return emojiList



        