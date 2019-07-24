import numpy as np
from neuralnetnode import NeuralNetNode
from mctspy.tree.search import MonteCarloTreeSearch
from cathedralstate import CathedralState
from sklearn.neural_network import MLPClassifier
from os import path
import os
from joblib import dump, load
from cathedral import Cathedral
import time

thisPath = path.dirname(path.realpath(__file__))

forClass = Cathedral.lightPlayer
numberOfGames = 400
startNN = 5
clf = None
clfRef = None

pickleNames = os.listdir(path.join(thisPath, 'pickles'))
sortedPickles = sorted(pickleNames,reverse=True)
gameFile = 'games'+str(int(time.time()))+'.data'

itFile = 'iteration.data'

startAt = 0

with open(path.join(thisPath, 'stats', itFile), 'r') as f:
    startAt = int(f.readline().strip())

if len(sortedPickles) == 0:
    clf = MLPClassifier(hidden_layer_sizes=(15,))#lbfgs is for smaller dataset
    clf.classes_ = [Cathedral.lightPlayer, Cathedral.darkPlayer, 0]#zero is draw
    
else:
    print (sortedPickles[0])
    clf = load(path.join(thisPath, 'pickles', sortedPickles[0]))
    if startAt > startNN:
        clfRef = clf

mctsIterations = 10

for g in range(startAt,numberOfGames):

    print ("game # ", g)

    keepGoing = True
    game = Cathedral()
    
    #randomize first move
    cathedralLegalMoves = game.getLegalMoves()
    index = np.random.randint(len(cathedralLegalMoves))
    initMove = cathedralLegalMoves[index]
    game.placePiece(initMove[0], initMove[1], initMove[2])
    
    state = None
    
    while keepGoing:
        #alternate which player uses the NN or strictly uses MCTS
        root = NeuralNetNode(CathedralState(game), clfRef, oneSided=(Cathedral.lightPlayer if g % 2 == 0 else Cathedral.darkPlayer))
        mcts = MonteCarloTreeSearch(root)
        best_node = mcts.best_action(mctsIterations)
        state = best_node.state
        game = state.game
        game.printIds()
        keepGoing = not best_node.state.game.isGameOver()
       
    inputData = state.raw(None)
    label = state.game_result
    
    # print ("light: ", game.getScore(Cathedral.lightPlayer))
    # print ("light remaining", game.lightPiecesLeft)
    # print ("dark: ", game.getScore(Cathedral.darkPlayer))
    # print ("dark remaining", game.darkPiecesLeft)
    
    with open(path.join(thisPath,'stats',gameFile), "a+") as f:
        f.write(' '.join([str(i) for i in inputData]))
        f.write('\r\n')
        f.write(str(label))
        f.write('\r\n')
    
    #clf.fit(train, labels)
    clf.partial_fit([inputData], [label])
    if g >= startNN:
        clfRef = clf
    
    if g % 5 == 0 and clfRef is not None:
        dump(clfRef, path.join(thisPath, 'pickles', 'C'+str(int(time.time())) + '.joblib'))     
        
    with open(path.join(thisPath, 'stats', itFile), 'w') as f:
        f.write(str(g+1))

if clfRef is not None:
    dump(clfRef, path.join(thisPath, 'pickles', 'C'+str(int(time.time())) + '.joblib'))     


