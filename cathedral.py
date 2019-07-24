class Cathedral:
    
    error = -1
    empty = 0
    wall = 102
    neutral = 1
    lightPlayer = 100
    darkPlayer = 101
    
    pieceData = [
        None,
        {
            'id' : 1,
            'value' : 6,
            'count' : 1,
            'directions' : ['N'],
            'dim' : [3,4],
            'prime' : 1,
            'shade': 'neutral',
            'name' : 'cathedral',
            'data' : [
                0,1,0,
                1,1,1,
                0,1,0,
                0,1,0
                ]
        },
        {
            'id' : 2,
            'value' : 1,
            'count' : 2,
            'directions' : ['N'],
            'dim' : [1,1],
            'prime' : 0,
            'shade' : 'light',
            'name' : 'tavern',
            'data' : [1]
        },
        {
            'id' : 3,
            'value' : 1,
            'count' : 2,
            'directions' : ['N'],
            'dim' : [1,1],
            'prime' : 0,
            'shade' : 'dark',
            'name' : 'tavern',                    
            'data' : [1]
        },
        {
            'id' : 4,
            'value' : 2,
            'count' : 2,
            'directions' : ['N','E'],
            'dim' : [1,2],
            'prime' : 0,
            'shade' : 'light',
            'name' : 'stable',
            'data' : [
                1,
                1
                ]
        },
        {
            'id' : 5,
            'value' : 2,
             'count' : 2,
            'directions' : ['N','E'],
            'dim' : [1,2],
            'prime' : 0,
            'shade' : 'dark',
            'name' : 'stable',                                        
            'data' : [
                1,
                1
                ]
        },
        {
            'id' : 6,
            'value' : 3,
            'count' : 2,
            'directions' : ['N','E','S','W'],
            'dim' : [2,2],
            'prime' : 0,
            'shade' : 'light',
            'name' : 'inn',                    
            'data' : [
                1,0,
                1,1
                ]
        },
        {
            'id' : 7,
            'value' : 3,
            'count' : 2,
            'directions' : ['N','E','S','W'],
            'dim' : [2,2],
            'prime' : 0,
            'shade' : 'dark',
            'name' : 'inn',                                        
            'data' : [
                1,0,
                1,1
                ]
        },
        {
            'id' : 8,
            'value' : 3,
            'count' : 1,
            'directions' : ['N','E'],
            'dim' : [1,3],
            'prime' : 0,
            'shade' : 'light',
            'name' : 'bridge',                    
            'data' : [
                1,
                1,
                1
                ]
        },
        {
            'id' : 9,
            'value' : 3,
            'count' : 1,
            'directions' : ['N','E'],
            'dim' : [1,3],
            'prime' : 0,
            'shade' : 'dark',
            'name' : 'bridge',                                        
            'data' : [
                1,
                1,
                1
                ]
        },
        {
            'id' : 10,
            'value' : 4,
            'count' : 1,
            'directions' : ['N'],
            'dim' : [2,2],
            'prime' : 0,
            'shade' : 'light',
            'name' : 'square',                    
            'data' : [
                1,1,
                1,1
                ]
        },
        {
            'id' : 11,
            'value' : 4,
            'count' : 1,
            'directions' : ['N'],
            'dim' : [2,2],
            'prime' : 0,
            'shade' : 'dark',
            'name' : 'square',                                        
            'data' : [
                1,1,
                1,1
                ]
        },
        {
            'id' : 12,
            'value' : 4,
            'count' : 1,
            'directions' : ['N','E'],
            'dim' : [2,3],
            'prime' : 0,
            'shade' : 'light',
            'name' : 'abby',                    
            'data' : [
                1,0,
                1,1,
                0,1
                ]
        },
        {
            'id' : 13,
            'value' : 4,
            'count' : 1,
            'directions' : ['N','E'],
            'dim' : [2,3],
            'prime' : 1,
            'shade' : 'dark',
            'name' : 'abby',                                        
            'data' : [
                0,1,
                1,1,
                1,0
                ]
        },
        {
            'id' : 14,
            'value' : 4,
            'count' : 1,
            'directions' : ['N','E','S','W'],
            'dim' : [3,2],
            'prime' : 1,
            'shade' : 'light',
            'name' : 'manor',                    
            'data' : [
                0,1,0,
                1,1,1
                ]
        },
        {
            'id' : 15,
            'value' : 4,
            'count' : 1,
            'directions' : ['N','E','S','W'],
            'dim' : [3,2],
            'prime' : 1,
            'shade' : 'dark',
            'name' : 'manor',                                        
            'data' : [
                0,1,0,
                1,1,1
                ]
        },
        {
            'id' : 16,
            'value' : 5,
            'count' : 1,
            'directions' : ['N','E','S','W'],
            'dim' : [3,3],
            'prime' : 2,
            'shade' : 'light',
            'name' : 'tower',                    
            'data' : [
                0,0,1,
                0,1,1,
                1,1,0
                ]
        },
        {
            'id' : 17,
            'value' : 5,
            'count' : 1,
            'directions' : ['N','E','S','W'],
            'dim' : [3,3],
            'prime' : 2,
            'shade' : 'dark',
            'name' : 'tower',                                        
            'data' : [
                0,0,1,
                0,1,1,
                1,1,0
                ]
        },
        {
            'id' : 18,
            'value' : 5,
            'count' : 1,
            'directions' : ['N'],
            'dim' : [3,3],
            'prime' : 4,
            'shade' : 'light',
            'name' : 'infirmary',                    
            'data' : [
                0,1,0,
                1,1,1,
                0,1,0
                ]
        },
        {
            'id' : 19,
            'value' : 5,
            'count' : 1,
            'directions' : ['N'],
            'dim' : [3,3],
            'prime' : 4,
            'shade' : 'dark',
            'name' : 'infirmary',                                        
            'data' : [
                0,1,0,
                1,1,1,
                0,1,0
                ]
        },
        {
            'id' : 20,
            'value' : 5,
            'count' : 1,
            'directions' : ['N','E','S','W'],
            'dim' : [2,3],
            'prime' : 1,
            'shade' : 'light',
            'name' : 'castle',                    
            'data' : [
                1,1,
                1,0,
                1,1
                ]
        },
        {
            'id' : 21,
            'value' : 5,
            'count' : 1,
            'directions' : ['N','E','S','W'],
            'dim' : [2,3],
            'prime' : 1,
            'shade' : 'dark',
            'name' : 'castle',                                        
            'data' : [
                1,1,
                1,0,
                1,1
                ]
        },
        {
            'id' : 22,
            'value' : 5,
            'count' : 1,
            'directions' : ['N','E','S','W'],
            'dim' : [3,3],
            'prime' : 1,
            'shade' : 'light',
            'name' : 'academy',                    
            'data' : [
                0,1,0,
                1,1,0,
                0,1,1
                ]
        },
        {
            'id' : 23,
            'value' : 5,
             'count' : 1,
            'directions' : ['N','E','S','W'],
            'dim' : [3,3],
            'prime' : 1,
            'shade' : 'dark',
            'name' : 'academy',                                        
            'data' : [
                0,1,0,
                0,1,1,
                1,1,0
                ]
        }
    ]
    
    def __init__(self, toCopy = None):
        
        if toCopy is None:
            self.next = Cathedral.lightPlayer
            self.board = [0]*144
            self.turn = 0
            self.lightPiecesLeft = []
            self.darkPiecesLeft = []
            self.state = []
            self.reset()
        else:
            self.next = toCopy.next
            self.board = list(toCopy.board)
            self.turn = toCopy.turn
            self.lightPiecesLeft = list(toCopy.lightPiecesLeft)
            self.darkPiecesLeft = list(toCopy.darkPiecesLeft)
            self.state = list(toCopy.state)
        
    def reset(self):
        self.board = [0]*144
        self.turn = 0
        for i in range(0,12):
            self.board[i] = Cathedral.wall
            self.board[144 - i - 1] = Cathedral.wall
            self.board[i*12] = Cathedral.wall
            self.board[(i+1)*12 - 1] = Cathedral.wall
            
        for id in range(2,24,2):
            p = Cathedral.pieceData[id]
            for i in range(0, p['count']):
                self.lightPiecesLeft.append(id)
        
        for id in range(3,24,2):
            p = Cathedral.pieceData[id]
            for i in range(0, p['count']):
                self.darkPiecesLeft.append(id)

    
    def _onBoard(self, pos):
        return not (pos[0] < 0 or pos[0] > 11 or pos[1] < 0 or pos[1] > 11)
    
    def _getBoardIndex(self, pos):
        if not self._onBoard(pos):
            return int(Cathedral.error)
        
        return int(pos[1]*12+pos[0])
    
    def isGameOver(self):
        return self.next == 0
    
    def _nextMove(self):
        if self.turn == 0:
            return Cathedral.lightPlayer
        
        lightMoves = False
        for id in self.lightPiecesLeft:
            if lightMoves: break
            piece = self.pieceData[id]
            for direction in piece['directions']:
                if lightMoves: break
                for i in range(1,11):
                    if lightMoves: break
                    for j in range(1,11):
                        if self.canPlacePiece(id, (i,j), direction):
                            lightMoves = True
                            break
        
        darkMoves = False
        for id in self.darkPiecesLeft:
            if darkMoves: break
            piece = self.pieceData[id]
            for direction in piece['directions']:
                if darkMoves: break
                for i in range(1,11):
                    if darkMoves: break
                    for j in range(1,11):
                        if self.canPlacePiece(id, (i,j), direction):
                            darkMoves = True
                            break
        
        if lightMoves and darkMoves:
            return Cathedral.lightPlayer if self.turn % 2 == 0 else Cathedral.darkPlayer
        
        if lightMoves:
            return Cathedral.lightPlayer
        
        if darkMoves:
            return Cathedral.darkPlayer
        
        return 0
    
    def getLegalMoves(self):
        
        if self.turn == 0:
            neturalMoves = []
            for i in range(1,11):
                for j in range(1,11):
                    if self.canPlacePiece(Cathedral.neutral, (i,j), "N"):
                        neturalMoves.append((Cathedral.neutral, (i,j), "N"))
            
            return neturalMoves
        
        neturalPos = []
        darkPos = []
        lightPos = []
        
        for i in range(1,11):
            for j in range(1,11):
                pos = (i,j)
                val = self.board[self._getBoardIndex(pos)]
                if val == Cathedral.empty:
                    neturalPos.append(pos)
                elif val == Cathedral.lightPlayer:
                    lightPos.append(pos)
                elif val == Cathedral.darkPlayer:
                    darkPos.append(pos)
        
        lightMoves = []
        
        for id in self.lightPiecesLeft:
            piece = self.pieceData[id]
            for direction in piece['directions']:
                for pos in neturalPos:
                    if self.canPlacePiece(id, pos, direction):
                        lightMoves.append((id, pos, direction))
        
        if len(lightMoves) == 0:
            for id in self.lightPiecesLeft:
                piece = self.pieceData[id]
                for direction in piece['directions']:
                    for pos in lightPos:
                        if self.canPlacePiece(id, pos, direction):
                            lightMoves.append((id, pos, direction))
        
        darkMoves = []
        for id in self.darkPiecesLeft:
            piece = self.pieceData[id]
            for direction in piece['directions']:
                for pos in neturalPos:
                    if self.canPlacePiece(id, pos, direction):
                        darkMoves.append((id, pos, direction))
        
        if len(darkMoves) == 0:
            for id in self.darkPiecesLeft:
                piece = self.pieceData[id]
                for direction in piece['directions']:
                    for pos in darkPos:
                        if self.canPlacePiece(id, pos, direction):
                            darkMoves.append((id, pos, direction))
        
        if len(lightMoves) > 0 and len(darkMoves) > 0:
            return darkMoves if self.turn % 2 == 1 else lightMoves
        
        if len(lightMoves) != 0:
            return lightMoves
        
        if len(darkMoves) != 0:
            return darkMoves
        
        return []
    
    def spaceOwnedBy(self, pos, b = None):
        
        b = b if b != None else self.board
        
        index = self._getBoardIndex(pos)
        
        if index == Cathedral.error:
            return index
        
        val = b[index]
        if (val == Cathedral.empty or val == Cathedral.neutral or val == Cathedral.wall):
            return val
        
        return Cathedral.lightPlayer if val % 2 == 0 else Cathedral.darkPlayer
    
    pieceChars = " +tTsSiIbBsSaAmMwWxXcCyY"
    
    def printIds(self):
        for i in range(0,144):
            val = self.board[i]
            
            if i % 12 == 0: 
                print ("", flush=True)
            
            if val == Cathedral.wall:
                print ('#', end = "")
            elif val == Cathedral.lightPlayer:
                print ('.', end = "")
            elif val == Cathedral.darkPlayer:
                print ('*', end = "")
            else:
                print(Cathedral.pieceChars[val], end="")
        
        print ("", flush=True)
            
    def getScore(self, player):
        
        coll = self.lightPiecesLeft if player % 2 == 0 else self.darkPiecesLeft

        total = 0
        for id in coll:
            total += int(self.pieceData[id]['value'])
        
        return total
    
    neighbors = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1), (0,0)]
    
    def floodTerritories(self, pieceParity, upperLeft, bottomRight, b):
        
        globalFlood = set({})
        isolatedFloods = []
        for i in range(int(upperLeft[0]),int(bottomRight[0]+1)):
            for j in range(int(upperLeft[1]),int(bottomRight[1]+1)):
                if self.spaceOwnedBy((i,j), b) != Cathedral.empty:
                    continue
                
                flood = set({})
                ids = []
                self.floodFromSinglePoint(pieceParity, i, j, globalFlood, flood, ids, b)
                
                if len(flood) > 0:    
                    isolatedFloods.append((flood, ids))
        
        removedIds = []
        capturedArea = 0
        
        for flood in isolatedFloods:
            #more than 1 other id found during flooding
            ids = {}
            for v in flood[1]:
                if v > 23 or v == 0:
                    continue
                
                if not v in ids:
                    ids[v] = 0
                ids[v] += 1
               
            subRemovedIds = []
            for id in ids:
                pId = int(id)
                
                subRemovedIds.extend([pId]*int(ids[pId] / int(self.pieceData[pId]['value'])))
            
            if len(subRemovedIds) <= 1:
                capturedArea += len(flood[0])
                removedIds.extend(subRemovedIds)
                for pos in flood[0]:
                    index = self._getBoardIndex(pos)
                    id = b[index]
                    b[index] = Cathedral.lightPlayer if pieceParity % 2 == 0 else Cathedral.darkPlayer
        
        return (removedIds, capturedArea)
        
        
    
    def floodFromSinglePoint(self, pieceParity, i, j, globalFlood, isolatedFlood, ids, b):
        b = b if b != None else self.board
        
        for n in Cathedral.neighbors:
            test = (n[0] + i, n[1] + j)
            
            #not on board
            if not self._onBoard(test):
                continue
            
            #already flooded to this point
            if test in globalFlood:
                continue
            
            id = b[self._getBoardIndex((test[0],test[1]))]
            
            #stop if hit a wall or a owned square
            isWall = id == Cathedral.wall
            isOwnedOrClaimed = (id % 2 == pieceParity % 2) and id != Cathedral.neutral and id != Cathedral.empty
            
            isOppentBuilding = id != Cathedral.empty and id != Cathedral.wall and id != Cathedral.darkPlayer and id != Cathedral.lightPlayer and (id % 2 != pieceParity % 2) and id != Cathedral.neutral
            
            if isWall or isOwnedOrClaimed:
                continue
            
            if isOppentBuilding or id == Cathedral.neutral:
                ids.append(id)

            globalFlood.add(test)
            isolatedFlood.add(test)
            
            #avoid infinite recursion
            if test == (0,0):
                continue
            
            self.floodFromSinglePoint(pieceParity, test[0], test[1], globalFlood, isolatedFlood, ids, b)

    
    def canPlacePiece(self, pieceId, pos, direction):
        #first turn must be the cathedral
        if self.turn == 0 and pieceId != Cathedral.neutral:
            return False
        
        pieceData = self.pieceData[pieceId]
        prime = pieceData['prime']
        data = pieceData['data']
        
        oldDim = pieceData['dim']
        dim = list(oldDim) if direction == 'N' or direction == 'S' else oldDim[::-1]
        
        primePos = self._shiftPos( (prime % oldDim[0], (prime - (prime % oldDim[0]))/oldDim[1]), direction, oldDim)
        startPos = ( pos[0] - primePos[0], pos[1] - primePos[1])
        
        if startPos[0] < 0 or startPos[0]+dim[0] > 11 or startPos[1] < 0 or startPos[1]+dim[1] > 11:
            return False
        
        for i in range(0,dim[0]):
            for j in range(0,dim[1]):
                
                #if piece data is 0, then it's a non-block square
                newPos = self._shiftPos((i,j), direction, dim, True)
                
                if data[newPos[0]+newPos[1]*oldDim[0]] == 0:
                    continue
                
                readPos = (startPos[0] + i, startPos[1] + j)
                boardIndex = self._getBoardIndex(readPos)
                
                val = self.board[boardIndex]
                
                #if the board is 0 here, it's ok and continue
                if val == Cathedral.empty:
                    continue
                
                #now determine that's a claimed but no buildings yet
                #values less than 100 are buildings
                #100 and 101 are claimed territory
                #if the territory and the piece id are the same parity
                #then the space it ok to place
                if val >= 100 and val != Cathedral.wall and ((val % 2) == (pieceId % 2)):
                    continue
                
                return False
        
        return True
    
    def _shiftPos(self, pos, direction, dim, inverse = False):
        ri = None
        rj = None
        
        if direction == "N":
            ri = pos[0]
            rj = pos[1]
        elif (direction == "E" and not inverse) or (direction == "W" and inverse):
            ri = dim[1] - pos[1] - 1
            rj = pos[0]
        elif direction == "S":
            ri = dim[0] - pos[0] - 1
            rj = dim[1] - pos[1] - 1
        elif (direction == "W" and not inverse) or (direction == "E" and inverse):
            ri = pos[1]
            rj = dim[0] - pos[0] - 1
            
        return (ri, rj)
    
    def placePiece(self, pieceId, pos, direction, commit = True):
        pieceData = self.pieceData[pieceId]
        prime = pieceData['prime']
        data = pieceData['data']
        
        oldDim = pieceData['dim']
        dim = list(oldDim) if direction == 'N' or direction == 'S' else oldDim[::-1]
        
        primePos = self._shiftPos( (prime % oldDim[0], (prime - (prime % oldDim[0]))/oldDim[1]), direction, oldDim)
        startPos = ( pos[0] - primePos[0], pos[1] - primePos[1])
        
        b = self.board if commit else list(self.board)
        
        for i in range(0,dim[0]):
            for j in range(0,dim[1]):
                
                writePos = (startPos[0] + i, startPos[1] + j)
                boardIndex = self._getBoardIndex(writePos)
                
                newPos = self._shiftPos((i,j), direction, dim, True)
                
                val = pieceId if data[newPos[0]+newPos[1]*oldDim[0]] == 1 else 0
                
                if val == 0:
                    continue
                
                b[boardIndex] = val# b[boardIndex] | val
        
        results = ([], 0, b)
        
        if self.turn > 1:
            upperLeft = (startPos[0] - 1, startPos[1] - 1)
            bottomRight = (startPos[0] + dim[0], startPos[1] + dim[1])
            tt = self.floodTerritories(pieceId % 2, upperLeft, bottomRight, b)
            results = (tt[0], tt[1], b)
        
        if commit:    
            self.turn += 1
            self.state.append((pieceId, pos, direction))
            
            if pieceId != Cathedral.neutral and pieceId != Cathedral.empty and pieceId % 2 == 0:
                self.lightPiecesLeft.remove(pieceId)
            elif pieceId != Cathedral.neutral and pieceId != Cathedral.empty and pieceId % 2 == 1:
                self.darkPiecesLeft.remove(pieceId)
            
            for removedId in results[0]:
                if removedId == Cathedral.empty or removedId == Cathedral.neutral:
                    continue
                if removedId % 2 == 0:
                    self.lightPiecesLeft.append(removedId)
                else:
                    self.darkPiecesLeft.append(removedId)
        
            self.next = self._nextMove()
        
        return results