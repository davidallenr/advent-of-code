# open the example file
with open('input.txt', 'r') as f:
    # read the file
    lines = f.readlines()

# initialize the total and the list of highest totals
score = 0

# enum for rock, paper, scissors
RPS_MAP_OPONNENT = {'rock': 'A', 'paper': 'B', 'scissors': 'C'}
RPS_MAP_OUTCOME = {'lose': 'X', 'draw': 'Y', 'win': 'Z'}

# map rock paper scissors to numbers to values
RPS_MAP = {'rock': 1, 'paper': 2, 'scissors': 3}   

# map win, lose, tie to numbers
WLT_MAP = {'win': 6, 'lose': 0, 'tie': 3}



# loop through the lines
for line in lines:
    # split the line for example A Y
    # would be split into ['A', 'Y']
    line = line.split()
    # get the opponent's move
    opponent_move = line[0]

    turn_outcome = line[1]

    # if the opponent's move is rock
    if opponent_move == RPS_MAP_OPONNENT['rock']:
        # if the turn outcome is win
        if turn_outcome == RPS_MAP_OUTCOME['win']:
            # add 6 to the score
            score += WLT_MAP['win'] + RPS_MAP['paper']
        # if the turn outcome is lose
        elif turn_outcome == RPS_MAP_OUTCOME['lose']:
            # add 0 to the score
            score += WLT_MAP['lose'] + RPS_MAP['scissors']
        # if the turn outcome is draw
        elif turn_outcome == RPS_MAP_OUTCOME['draw']:
            # add 3 to the score
            score += WLT_MAP['tie'] + RPS_MAP['rock']
    # if the opponent's move is paper
    elif opponent_move == RPS_MAP_OPONNENT['paper']:
        # if the turn outcome is win
        if turn_outcome == RPS_MAP_OUTCOME['win']:
            # add 6 to the score
            score += WLT_MAP['win'] + RPS_MAP['scissors']
        # if the turn outcome is lose
        elif turn_outcome == RPS_MAP_OUTCOME['lose']:
            # add 0 to the score
            score += WLT_MAP['lose'] + RPS_MAP['rock']
        # if the turn outcome is draw
        elif turn_outcome == RPS_MAP_OUTCOME['draw']:
            # add 3 to the score
            score += WLT_MAP['tie'] + RPS_MAP['paper']
    # if the opponent's move is scissors
    elif opponent_move == RPS_MAP_OPONNENT['scissors']:
        # if the turn outcome is win
        if turn_outcome == RPS_MAP_OUTCOME['win']:
            # add 6 to the score
            score += WLT_MAP['win'] + RPS_MAP['rock']
        # if the turn outcome is lose
        elif turn_outcome == RPS_MAP_OUTCOME['lose']:
            # add 0 to the score
            score += WLT_MAP['lose'] + RPS_MAP['paper']
        # if the turn outcome is draw
        elif turn_outcome == RPS_MAP_OUTCOME['draw']:
            # add 3 to the score
            score += WLT_MAP['tie'] + RPS_MAP['scissors']
            
    
    # all rock paper scissors combinations
    # rock vs rock
    # if opponent_move == RPS_MAP_OPONNENT['rock'] and player_move == RPS_MAP_PLAYER['rock']:
    #     score += WLT_MAP['tie'] + RPS_MAP['rock']
    # # rock vs paper
    # elif opponent_move == RPS_MAP_OPONNENT['rock'] and player_move == RPS_MAP_PLAYER['paper']:
    #     score += WLT_MAP['win'] + RPS_MAP['paper']
    # # rock vs scissors
    # elif opponent_move == RPS_MAP_OPONNENT['rock'] and player_move == RPS_MAP_PLAYER['scissors']:
    #     score += WLT_MAP['lose'] + RPS_MAP['scissors']
    # # paper vs rock
    # elif opponent_move == RPS_MAP_OPONNENT['paper'] and player_move == RPS_MAP_PLAYER['rock']:
    #     score += WLT_MAP['lose'] + RPS_MAP['rock']
    # # paper vs paper
    # elif opponent_move == RPS_MAP_OPONNENT['paper'] and player_move == RPS_MAP_PLAYER['paper']:
    #     score += WLT_MAP['tie'] + RPS_MAP['paper']
    # # paper vs scissors
    # elif opponent_move == RPS_MAP_OPONNENT['paper'] and player_move == RPS_MAP_PLAYER['scissors']:
    #     score += WLT_MAP['win'] + RPS_MAP['scissors']
    # # scissors vs rock
    # elif opponent_move == RPS_MAP_OPONNENT['scissors'] and player_move == RPS_MAP_PLAYER['rock']:
    #     score += WLT_MAP['win'] + RPS_MAP['rock']
    # # scissors vs paper
    # elif opponent_move == RPS_MAP_OPONNENT['scissors'] and player_move == RPS_MAP_PLAYER['paper']:
    #     score += WLT_MAP['lose'] + RPS_MAP['paper']
    # # scissors vs scissors
    # elif opponent_move == RPS_MAP_OPONNENT['scissors'] and player_move == RPS_MAP_PLAYER['scissors']:
    #     score += WLT_MAP['tie'] + RPS_MAP['scissors']

    # if the score is less than 0
    if score < 0:
        # set the score to 0
        score = 0
        
print(score)