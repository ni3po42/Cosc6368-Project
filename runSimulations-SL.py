import numpy as np
from mctspy.tree.search import MonteCarloTreeSearch
from mctspy.tree.nodes import TwoPlayersGameMonteCarloTreeSearchNode
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
clf = None

pickleNames = os.listdir(path.join(thisPath, 'sl-pickles-11'))
sortedPickles = sorted(pickleNames,reverse=True)
gameFile = 'slGames'+str(int(time.time()))+'.data'

itFile = 'iteration.data'
startAt = 0

with open(path.join(thisPath, 'sl-stats-11', itFile), 'r') as f:
    startAt = int(f.readline().strip())

if len(sortedPickles) == 0:
    clf = MLPClassifier(hidden_layer_sizes=(15,))#lbfgs is for smaller dataset
    clf.classes_ = [Cathedral.lightPlayer, Cathedral.darkPlayer, 0]#zero is draw
else:
    print (sortedPickles[0])
    clf = load(path.join(thisPath, 'sl-pickles-11', sortedPickles[0]))

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
        root = TwoPlayersGameMonteCarloTreeSearchNode(CathedralState(game))
        mcts = MonteCarloTreeSearch(root)
        best_node = mcts.best_action(mctsIterations)
        state = best_node.state
        game = state.game
        game.printIds()
        keepGoing = not best_node.state.game.isGameOver()
       
    inputData = state.raw(None)
    label = state.game_result
    
    with open(path.join(thisPath,'sl-stats-11',gameFile), "a+") as f:
        f.write(' '.join([str(i) for i in inputData]))
        f.write('\r\n')
        f.write(str(label))
        f.write('\r\n')
    
    #clf.fit(train, labels)
    clf.partial_fit([inputData], [label])
    
    if g % 5 == 0:
        dump(clf, path.join(thisPath, 'sl-pickles-11', 'CSL'+str(int(time.time())) + '.joblib'))     
        
    with open(path.join(thisPath, 'sl-stats-11', itFile), 'w') as f:
        f.write(str(g+1))

dump(clf, path.join(thisPath, 'sl-pickles-11', 'SLC'+str(int(time.time())) + '.joblib')) 