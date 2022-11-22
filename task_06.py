class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players=None):
    if not players or len(players) != 2:
        raise WrongNumberOfPlayersError

    my_dict = {('R', 'P'): 'player2', ('P', 'R'): 'player1', ('R', 'S'): 'player1', ('S', 'R'): 'player2', ('S', 'P'): 'player1', ('P', 'S'): 'player2'}

    for item in players:
        if item[1] not in ('R', 'P', 'S'):
            raise NoSuchStrategyError
    else:
        bits = []
        for item in players:
            bits.append(item[1])

    if bits[0] == bits[1]:
        return f'player1 {bits[0]}'

    for key, value in my_dict.items():
        if list(key) == bits:
            return f'{value} {bits[int(value[-1])-1]}'
