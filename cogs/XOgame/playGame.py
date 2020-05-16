from cogs.XOgame.utils import XOgame


player1 = input("Enter username of player1 :")
player2 = input("Enter username of player1 :")


game = XOgame(player1,player2)
game.new_grid()

print(game.show_grid())

while True:
        if not game.is_won():
                if not game.ended():
                        ask1 = input(f"{player1} please enter the box you want to fill:")
                        game.fill_x(int(ask1))
                        print(game.show_grid())
                else:
                        break


        else:
                break

        if not game.is_won():
                if not game.ended():
                        ask2 = input(f"{player2} please enter the box you want to fill:")
                        game.fill_o(int(ask2))
                        print(game.show_grid())
                        #print(game.is_won())
                else:
                        break


        else:
                break






