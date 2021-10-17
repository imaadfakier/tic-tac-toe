from IPython.display import clear_output


def who_goes_first():
    acceptable_input = ['X', 'O', 'x', 'o']
    players = ()
    player_choice = ''
    while player_choice not in acceptable_input:
        player_choice = input('Player 1: Do you want to be X or O? ')
    else:
        if player_choice == 'X' or player_choice == 'x':
            # no return statement as no assignment happens
            print('Player 1 will go first.')
            players = ('X', 'O')
        else:
            print('Player 2 will go first.')
            players = ('O', 'X')
    return players


def confirm_game_start(grid):
    acceptable_input = ['Yes', 'No']
    player_confirmation = input('Are you ready to play? Enter Yes or No. ')
    while player_confirmation not in acceptable_input:
        player_confirmation = input('Are you ready to play? Enter Yes or No. ')
    else:
        if player_confirmation == 'Yes':
            display_game_grid(grid)
    return player_confirmation


def display_game_grid(grid):
    clear_output()
    print(grid[7] + ' | ' + grid[8] + ' | ' + grid[9])
    print('--|---|--')
    print(grid[4] + ' | ' + grid[5] + ' | ' + grid[6])
    print('--|---|--')
    print(grid[1] + ' | ' + grid[2] + ' | ' + grid[3])


def start_game(grid, players):
    acceptable_input = list(range(0, 10))
    player_one, player_two = players
    current_player_turn = ''
    if players == ('X', 'O'):
        current_player_turn = player_one
    elif players == ('O', 'X'):
        current_player_turn = player_two
    game_has_ended = False
    winner_found = False
    player_position = ''
    while not game_has_ended:
        while player_position not in acceptable_input:
            player_position = input('Choose your next position: (1-9) ')
            if player_position.isdigit():
                player_position = int(player_position)
        acceptable_input.pop(acceptable_input.index(player_position))
        current_player_turn, game_has_ended, winner_found = find_winner_or_declare_draw(grid, player_position, current_player_turn, game_has_ended, winner_found, player_one, player_two)
    else:
        if winner_found:
            if current_player_turn == 'x':
                print(f'Congratulations player one! You have won the game!')
            else:
                print(f'Congratulations player two! You have won the game!')
        else:
            print(f'Stalemate! The game is a tie.')


def find_winner_or_declare_draw(grid, player_position, current_player_turn, game_has_ended, winner_found, player_one, player_two):
    grid[player_position] = current_player_turn
    display_game_grid(grid)
    if (grid[7] == grid[8] == grid[9] == current_player_turn) or (grid[4] == grid[5] == grid[6] == current_player_turn) or (grid[1] == grid[2] == grid[3] == current_player_turn) or (grid[1] == grid[5] == grid[9] == current_player_turn) or (grid[3] == grid[5] == grid[7] == current_player_turn) or (grid[1] == grid[4] == grid[7] == current_player_turn) or (grid[2] == grid[5] == grid[8] == current_player_turn) or (grid[3] == grid[6] == grid[9] == current_player_turn):
        game_has_ended = True
        winner_found = True
    elif ' ' not in grid:
        game_has_ended = True
    elif current_player_turn == player_one:
        current_player_turn = player_two
    elif current_player_turn == player_two:
        current_player_turn = player_one
    return (current_player_turn, game_has_ended, winner_found)


def play_tic_tac_toe(grid):
    print('Welcome to Tic Tac Toe!')
    display_game_grid(grid)
    players = who_goes_first()
    if confirm_game_start(grid) == 'Yes':
        start_game(grid, players)
    else:
        return f'Game has been canceled.'


grid = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
acceptable_input = ['Yes', 'No', 'yes', 'no']
play_again = ''
while play_again != 'No':
    play_tic_tac_toe(grid)
    while play_again not in acceptable_input:
        play_again = input('Do you want to play again? Enter Yes or No: ')
    if play_again == 'Yes' or play_again == 'yes':
        play_again = ''
        clear_output()
        grid = [' '] * 10
