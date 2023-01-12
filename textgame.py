##parislucas
def game_rules():   ##welcomes user to game and explains the rules and moves
    print('*************************************************************')
    print('              ***WELCOME TO WITCH ESCAPE***')
    print('*************************************************************\n')
    print('You must travel throughout the house to collect all the ingredients needed to cast a spell upon your EVIL twin sister ELIZABETH so you can regain your powers!\n'
          'Starting in the library, you will enter a move-- north, south, east or west-- to travel to different rooms and collect items, adding them to your bag. \n'
          "You must type 'voila' to pick up the item, otherwise it will be left behind and you'll have to circle back for it.\n"
          'Be careful, if you run into Elizabeth before you collect all 6 items...GAME OVER!\n'
          "You can type 'exit' to quit or '?' for help.\n"
          "*************************************************************\n")
def help():  #this function, accessed by '?' gives user a quick guide of valid input options in case they need help
    print('valid moves to travel =  north, south, east, west.   pick up an item = voila.  quit = exit')
    print('*************************************************************\n')

def end_game(player_location): # this function defines 2 possible ends to the game
    if len(player_inventory) == 6:   #if the player collects all 6 items, they win. game ends
        print("CONGRATULATIONS, YOU'VE RETRIEVED ALL THE ITEMS TO MAKE YOUR POTION! YOUR EVIL TWIN IS GOING DOWN!!!!")
    elif player_location == "Elizabeth's bathroom": #if the player enters the room with elizabeth, they lose. game ends
        print("YOU DON'T HAVE ENOUGH ITEMS TO CAST YOUR SPELL...GAME OVER!!!!")

def player_status():  ##creates function to show play location and inventory
  print('You are now in {}'.format(player_location))
  print('Your bag contains: ', player_inventory)

def manage_items():  ##creates function to show items in room and allow user to pick up and add to bag
    if valid_directions[player_location]['item'] == 'no item' or valid_directions[player_location][
        'item'] in player_inventory:  ##if no item exists in room or item already picked up..display there is no item to pick up
        print('There is no item in this room to pick up.')
        print('*************************************************************')
    else:  ##prompt user to see if they will pick up item...if correct word entered, add to bag, otherwise the item stays
        pickup_item = input(("There's {}! GET IT! ".format(valid_directions[player_location]['item']))).lower()
        if pickup_item in ('voila'):
            player_inventory.append((valid_directions[player_location]['item']))
            print('Got it!', end=' ')
            print("{} is added to your bag. ".format(valid_directions[player_location]['item']))

            print('*************************************************************')
        else:
            print('You did not get the {}.'.format(valid_directions[player_location]['item']))
            print('*************************************************************')

##this dictionary defines all rooms, valid directions that can be taken from each room and the item stored in each room

valid_directions = {
        'the library': {'east': 'the living room', 'item': 'no item'},
        'the living room': {'north': "Giselle's room", 'east': 'the kitchen', 'west': 'the library',
                            'south': "Elizabeth's room", 'item': 'the candle'},
        "Giselle's room": {'south': 'the living room', 'east': "Giselle's bathroom", 'item': 'the crystal'},
        "Giselle's bathroom": {'west': "Giselle's room", 'item': 'the mirror'},
        'the dining room': {'south': 'the kitchen', 'item': 'the glass bowl'},
        'the kitchen': {'north': 'the dining room', 'west': 'the living room', 'item': 'the egg'},
        "Elizabeth's room": {'north': 'the living room', 'east': "Elizabeth's bathroom", 'item': 'the hair'},
        "Elizabeth's bathroom": {'item': 'elizabeth'}

}

##this list defines valid directions
possible_moves = ['north', 'south', 'east', 'west']
#starts the player in the room called 'the library'
player_location = 'the library'
#starts empty list to store player inventory
player_inventory = []
game_rules()
player_status()

while len(player_inventory) < 6:  ##loop until user gets all 6 items
    move = input('Make your move:  ').lower()
    if move == 'exit':  # if players move is Exit, the game is over
        print('You have exited the game. GOODBYE!')
        break
    elif move == '?':  ##if player enters help command, instructions show
        help()
    elif move not in possible_moves:  # if move is invalid direction altogether, let user know and give valid options
        print('INVALID MOVE!')
        help()
    elif move in possible_moves and move not in valid_directions[
        player_location]:  # if input is a valid command but not a valid direction to travel from the current room, output they cant travel that way
        print("OOPS! You've hit a wall.")
    else: ##if player enters a valid move, they move to the next room and player status is shown
        player_location = valid_directions[player_location][move]
        player_status()
        if valid_directions[player_location]['item'] == 'elizabeth':  ##if player runs into villain, endgame function executes
            print('OH NO, ELIZABETH IS HERE!')
            end_game(player_location)
            break
        else:
            manage_items()
if len(player_inventory) == 6:  ##if player gets all 6 items, endgame executes.
    end_game(player_location)


