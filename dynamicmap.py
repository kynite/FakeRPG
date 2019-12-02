map = [[None(0, 0), None(1, 0), 'Ethereal Lake'(2, 0), None(3, 0), None(4, 0)],
       [None(0, 1), None(1, 1), None(2, 1), None(3, 1), None(4, 1)],
       ['Juilot Lake'(0, 2), None(1, 2), None(2, 2), None(3, 2), 'Kytersize Lake'(4, 2)],
       [None(0, 3), None(1, 3), None(2, 3), None(3, 3), None(4, 3)],
       [None(0, 4), 'Where are we now lake'(1, 4), None(2, 4), 'Hooligan Lake'(3, 4), None(4, 4)],
       [None(0, 5), None(1, 5), 'Residential Lake'(2, 5), None(3, 5), None(4, 5)],
       [None(0, 6), None(1, 6), None(2, 6), 'Player'(3, 6), 'Home'(4, 6)]]


class Player:
    def __init__(self):
        self.x = 3
        self.y = 6




class MapTile:
    """map"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def modify_player(self, player):
        """Added modify_player to every tile"""
        pass
