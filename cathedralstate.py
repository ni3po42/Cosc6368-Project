import numpy as np
from mctspy.games.common import TwoPlayersAbstractGameState, AbstractGameAction

from cathedral import Cathedral

class CathedralState(TwoPlayersAbstractGameState):

    def __init__(self, game):
        self.game = game
        self.next_to_move = game.next

    @property
    def game_result(self):
        
        if not self.game.isGameOver():
            return None
        
        lightScore = self.game.getScore(Cathedral.lightPlayer)
        darkScore = self.game.getScore(Cathedral.darkPlayer)
        
        if lightScore < darkScore:
            return Cathedral.lightPlayer
            
        if darkScore < lightScore:
            return Cathedral.darkPlayer
        
        return 0

    def is_game_over(self):
        return self.game_result is not None

    def is_move_legal(self, move):
        id = move[0]
        pos = move[1]
        direction = move[2]
        
        return self.canPlacePiece(id, pos, direction)

    def move(self, move):
        
        id = move[0]
        pos = move[1]
        direction = move[2]
        
        newBoard = Cathedral(toCopy = self.game)
        
        if not newBoard.canPlacePiece(id, pos, direction):
            newBoard.printIds()
            print(move)
            raise ValueError("move is not legal")
        
        newBoard.placePiece(id, pos, direction)
        
        return CathedralState(newBoard)
     
    def raw(self, withMove):
        
        data = []
        b = self.game.board
        if withMove is not None:
            id = withMove[0]
            pos = withMove[1]
            direction = withMove[2]
            
            results = self.game.placePiece(id, pos, direction, False)
            b = results[2]
            
            
        for i in range(0,144):
            if (i%12 == 0 or i%12 == 11) or i < 12 or i > 131:
                continue
            data.append(self.game.board[i])
            
        return data
        
    def get_legal_actions(self):
        #flatten move data
        return self.game.getLegalMoves()