import unittest

from cathedral import Cathedral

class TestCathedral(unittest.TestCase):

    def _getId(self, piece):
        f = lambda x: x is not None and x['shade']==piece[0] and x['name'] == piece[1]
        return list(filter(f, Cathedral.pieceData))[0]['id']

    def test_canCreateGame(self):
        game = Cathedral()
        self.assertIsInstance(game, Cathedral)

    def test_firstMoveMustBeTheCathedral(self):
        game = Cathedral()
        
        result = game.canPlacePiece(self._getId(('neutral', 'cathedral')),(6,6),'N')
        self.assertTrue(result)
        
        result = game.canPlacePiece(self._getId(('light', 'tavern')),(6,6),'N')
        self.assertFalse(result)
        
    def test_gameStartWithWall(self):
        game = Cathedral()
        
        for i in range(0,12):
            self.assertEqual(game.spaceOwnedBy((0,i)), Cathedral.wall)
            self.assertEqual(game.spaceOwnedBy((11,i)), Cathedral.wall)
            self.assertEqual(game.spaceOwnedBy((i,0)), Cathedral.wall)
            self.assertEqual(game.spaceOwnedBy((i,11)), Cathedral.wall)
            
        for i in range(1,11):
            for j in range (1,11):
                self.assertEqual(game.spaceOwnedBy((i,j)), Cathedral.empty)
    
    def test_canShiftPos(self):
        game = Cathedral()
        dim = [2,3]
        
        pos = game._shiftPos((0,0), "N", dim)
        self.assertEqual(pos, (0,0))
        
        pos = game._shiftPos((0,0), "E", dim)
        self.assertEqual(pos, (2,0))
        
        pos = game._shiftPos((0,0), "S", dim)
        self.assertEqual(pos, (1,2))
        
        pos = game._shiftPos((0,0), "W", dim)
        self.assertEqual(pos, (0,1))
        
        ######################################
        pos = game._shiftPos((1,1), "N", dim)
        self.assertEqual(pos, (1,1))
        
        pos = game._shiftPos((1,1), "E", dim)
        self.assertEqual(pos, (1,1))
        
        pos = game._shiftPos((1,1), "S", dim)
        self.assertEqual(pos, (0,1))
        
        pos = game._shiftPos((1,1), "W", dim)
        self.assertEqual(pos, (1,0))
        
        
    
    def test_canPlacePieces(self):
        pieceData = Cathedral.pieceData
        game = Cathedral()
        
        for id in range(2,24):
            piece = pieceData[id]
            
            for direction in piece['directions']:
                game.reset()
                game.placePiece(Cathedral.neutral,(2,7), "N")
                oldBoard = list(game.board)
                game.placePiece(id,(5,5), direction)
                self.assertNotEqual(oldBoard, game.board)
                    
    def test_canTestToPlacePieces(self):
        pieceData = Cathedral.pieceData
        game = Cathedral()
        
        game.reset()
        game.placePiece(Cathedral.neutral,(2,7), "N")
        
        for id in range(2,24):
            piece = pieceData[id]
            
            for direction in piece['directions']:
                result = game.canPlacePiece(id,(5,5), direction)
                if not result:
                    print(piece, direction, game.turn)
                self.assertTrue(result)
        
        result = game.canPlacePiece(self._getId(('light', 'tavern')), (0,0), "N")
        self.assertFalse(result)
        
        for id in range(2,24):
            piece = pieceData[id]
              
            for direction in piece['directions']:
                
                result = game.canPlacePiece(id,(2,7), direction)
                self.assertFalse(result)
                    
    def test_canFlood(self):
        
        game = Cathedral()
        
        t = game.placePiece(self._getId(('neutral', 'cathedral')), (2,6), "N")
        game.printIds()
        self.assertEqual(len(t[0]), 0)
        self.assertEqual((t[1]), 0)
        
        self.assertTrue(self._getId(('dark','academy')) in game.darkPiecesLeft)
        
        t = game.placePiece(self._getId(('dark', 'academy')), (1,4), "W")
        game.printIds()
        self.assertEqual(len(t[0]), 0)
        self.assertEqual((t[1]), 0)
        
        self.assertFalse(self._getId(('dark', 'academy')) in game.darkPiecesLeft)
        
        
        self.assertTrue(self._getId(('light', 'bridge')) in game.lightPiecesLeft)
        
        t = game.placePiece(self._getId(('light', 'bridge')), (5,1), "N")
        game.printIds()
        self.assertEqual(len(t[0]), 0)
        self.assertEqual((t[1]), 0)
        
        self.assertFalse(self._getId(('light', 'bridge')) in game.lightPiecesLeft)
        
        
        t = game.placePiece(self._getId(('dark', 'castle')), (3,3), "S")
        game.printIds()
        self.assertEqual(len(t[0]), 0)
        self.assertEqual((t[1]), 6)
        t = game.placePiece(self._getId(('light', 'tower')), (8,5), "E")
        game.printIds()
        self.assertEqual(len(t[0]), 0)
        self.assertEqual((t[1]), 0)
        t = game.placePiece(self._getId(('dark', 'abby')), (6,1), "W")
        game.printIds()
        self.assertEqual(len(t[0]), 0)
        self.assertEqual((t[1]), 0)
        t = game.placePiece(self._getId(('light', 'inn')), (7,9), "N")
        game.printIds()
        self.assertEqual(len(t[0]), 0)
        self.assertEqual((t[1]), 0)
        t = game.placePiece(self._getId(('dark', 'square')), (9,3), "N")
        game.printIds()
        self.assertEqual(len(t[0]), 0)
        self.assertEqual((t[1]), 0) 
        t = game.placePiece(self._getId(('light', 'academy')), (8,6), "W")
        game.printIds()
        self.assertEqual(len(t[0]), 0)
        self.assertEqual((t[1]), 0)
        t = game.placePiece(self._getId(('dark', 'inn')), (4,7), "S")
        game.printIds()
        self.assertEqual(len(t[0]), 0)
        self.assertEqual((t[1]), 0)
        t = game.placePiece(self._getId(('light', 'inn')), (7,8), "W")
        game.printIds()
        self.assertEqual(len(t[0]), 0)
        self.assertEqual((t[1]), 8)
        t = game.placePiece(self._getId(('dark', 'tower')), (4,8), "W")
        game.printIds()
        self.assertEqual(len(t[0]), 1)
        self.assertTrue(1 in t[0])
        self.assertEqual((t[1]), 19)
        
    def test_doesNotRemove2OfSameBuilding(self):
        
        game = Cathedral()
        
        game.placePiece(self._getId(('neutral', 'cathedral')), (2,6), "N")
        
        game.placePiece(self._getId(('dark', 'academy')), (1,4), "W")
        
        game.placePiece(self._getId(('light', 'tavern')), (1,1), "N")
        
        game.placePiece(self._getId(('dark', 'tower')), (4,8), "W")
        
        game.placePiece(self._getId(('light', 'tavern')), (1,2), "N")
        
        t = game.placePiece(self._getId(('dark', 'castle')), (3,3), "S")
        self.assertEqual(len(t[0]), 1)
        self.assertTrue(1 in t[0])
        self.assertEqual((t[1]), 79)

    def test_returnsRemovedPieceToPlayer(self):
        
        game = Cathedral()
        
        game.placePiece(self._getId(('neutral', 'cathedral')), (2,6), "N")
        
        game.placePiece(self._getId(('dark', 'academy')), (1,4), "W")
        
        self.assertEqual(len( list(filter(lambda v : v == 2, game.lightPiecesLeft))  ), 2) 
        
        game.placePiece(self._getId(('light', 'tavern')), (1,1), "N")
        
        self.assertEqual(len( list(filter(lambda v : v == 2, game.lightPiecesLeft))  ), 1) 
        
        game.placePiece(self._getId(('dark', 'tower')), (4,8), "W")
        
        game.placePiece(self._getId(('light', 'tavern')), (10,10), "N")
        
        self.assertEqual(len( list(filter(lambda v : v == 2, game.lightPiecesLeft))  ), 0) 
        
        t = game.placePiece(self._getId(('dark', 'castle')), (3,3), "S")
        
        self.assertEqual(len( list(filter(lambda v : v == 2, game.lightPiecesLeft))  ), 1) 

    def test_commitVsNoCommit(self):
        
        game = Cathedral()
        
        b = list(game.board);
        r = game.placePiece(self._getId(('neutral', 'cathedral')), (2,6), "N", False)
        self.assertEqual(b, game.board)
        
        r = game.placePiece(self._getId(('neutral', 'cathedral')), (2,6), "N", True)
        self.assertNotEqual(b, game.board)
        

    def test_canReloadBoard(self):
        
        game = Cathedral()
        
        game.placePiece(self._getId(('neutral', 'cathedral')), (2,6), "N")
        game.placePiece(self._getId(('dark', 'academy')), (1,4), "W")
        
        newGame = Cathedral(game)
        
        self.assertListEqual(game.state, newGame.state)
        self.assertListEqual(game.board, newGame.board)
        
        self.assertListEqual(game.lightPiecesLeft, newGame.lightPiecesLeft)
        self.assertListEqual(game.darkPiecesLeft, newGame.darkPiecesLeft)
        
        self.assertEqual(game.turn, newGame.turn)
        
        pass

        
if __name__ == '__main__':
    unittest.main()