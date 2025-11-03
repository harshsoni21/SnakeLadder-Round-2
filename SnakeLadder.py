
import random
class Grid : 
    def __init__(self,n):
        self.grid = n * n
        
        

class Player:
    def __init__(self,name):
        self.name = name
        self.curr_position = 0
        self.dice_role_history = []
        self.position_history = []
        self.status = 0 # It will tell whether won or not 
        
custom_game = Grid(7)
p1 = Player("P1")
p2 = Player("P2")
p3 = Player("P3")
p4= Player("P4")

player_list = [p1,p2,p3,p4]


game_finish = False
while not game_finish:
    curr_player = player_list[0]
    dice_no = random.randint(1,6)
    
    # now check if player is exceeding extra 
    last_pos = curr_player.curr_position 
    
    # History of Dice Will be saved in every Condition
    curr_player.dice_role_history.append(dice_no)
    
    if last_pos + dice_no == custom_game.grid:
        curr_player.position_history.append(last_pos + dice_no)
        curr_player.status = 1
        curr_player.curr_position = last_pos + dice_no
        game_finish = True
    elif last_pos + dice_no < custom_game.grid:
        curr_player.position_history.append(last_pos + dice_no)
        curr_player.status = 0
        curr_player.curr_position = last_pos + dice_no
        
    
    player_list.pop(0)
    player_list.append(curr_player)
    
for it in player_list:
    print(it.__dict__)
    

