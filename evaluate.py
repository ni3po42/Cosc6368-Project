import numpy as np
from os import path
import os
from joblib import dump, load
from cathedral import Cathedral
import matplotlib.pyplot as plt
import sklearn.metrics

rc = sklearn.metrics.recall_score
pre = sklearn.metrics.precision_score

thisPath = path.dirname(path.realpath(__file__))

evaluationTestGames = [
    [(1, (9, 4), 'N'), (23, (8, 2), 'W'), (22, (8, 8), 'W'), (21, (8, 9), 'W'), (20, (5, 8), 'W'), (19, (7, 6), 'N'), (18, (7, 3), 'N'), (17, (4, 3), 'W'), (16, (2, 8), 'W'), (21, (4, 1), 'W'), (14, (4, 6), 'W'), (15, (2, 4), 'W'), (12, (3, 6), 'E'), (13, (3, 2), 'E'), (8, (1, 4), 'N'), (7, (1, 2), 'N'), (4, (8, 1), 'E'), (5, (6, 7), 'N'), (4, (4, 4), 'N'), (3, (10, 6), 'N'), (2, (10, 4), 'N'), (3, (10, 1), 'N'), (2, (9, 3), 'N'), (10, (1, 9), 'N'), (6, (9, 10), 'W'), (6, (7, 10), 'W')],
    [(1, (5, 7), 'N'), (23, (8, 8), 'W'), (22, (8, 5), 'W'), (21, (8, 2), 'W'), (20, (7, 9), 'W'), (19, (7, 4), 'N'), (18, (5, 5), 'N'), (17, (4, 1), 'W'), (16, (2, 8), 'W'), (15, (6, 7), 'W'), (22, (2, 4), 'W'), (13, (4, 7), 'E'), (14, (2, 2), 'W'), (11, (1, 9), 'N'), (8, (1, 6), 'N'), (9, (1, 3), 'N'), (6, (2, 1), 'E'), (5, (6, 9), 'N'), (2, (10, 10), 'N'), (3, (8, 9), 'N'), (2, (6, 6), 'N'), (3, (5, 3), 'N'), (7, (9, 6), 'W'), (7, (8, 5), 'W'), (5, (10, 1), 'E')],
    [(1, (3, 1), 'N'), (23, (8, 9), 'W'), (22, (7, 5), 'W'), (21, (8, 2), 'W'), (20, (7, 6), 'W'), (19, (6, 9), 'N'), (18, (6, 4), 'N'), (17, (5, 1), 'W'), (16, (4, 5), 'W'), (15, (3, 9), 'W'), (14, (2, 7), 'W'), (13, (3, 10), 'E'), (12, (3, 5), 'E'), (11, (1, 3), 'N'), (8, (10, 6), 'N'), (7, (4, 3), 'W'), (6, (5, 8), 'S'), (7, (2, 1), 'E'), (6, (1, 7), 'N'), (5, (8, 8), 'E'), (4, (10, 4), 'N'), (3, (8, 4), 'N'), (2, (4, 4), 'N'), (3, (4, 1), 'N'), (2, (1, 5), 'N'), (9, (10, 1), 'E'), (5, (9, 10), 'E')],
    [(1, (3, 3), 'N'), (23, (8, 8), 'W'), (22, (8, 5), 'W'), (21, (8, 1), 'W'), (20, (7, 9), 'W'), (19, (7, 7), 'N'), (18, (6, 4), 'N'), (17, (6, 2), 'W'), (16, (3, 8), 'W'), (15, (4, 7), 'W'), (14, (1, 9), 'W'), (13, (5, 2), 'E'), (12, (3, 2), 'E'), (11, (1, 6), 'N'), (8, (6, 8), 'N'), (7, (10, 3), 'E'), (6, (5, 5), 'E'), (7, (2, 1), 'E'), (4, (1, 4), 'N'), (5, (5, 3), 'E'), (4, (10, 6), 'N'), (3, (10, 10), 'N'), (2, (8, 9), 'N'), (3, (8, 6), 'N'), (2, (7, 5), 'N'), (9, (7, 1), 'E'), (6, (3, 9), 'N')],
    [(1, (4, 4), 'N'), (23, (8, 9), 'W'), (22, (8, 5), 'W'), (21, (8, 1), 'W'), (20, (7, 3), 'W'), (19, (8, 7), 'N'), (18, (6, 8), 'N'), (17, (5, 4), 'W'), (16, (4, 1), 'W'), (21, (5, 9), 'W'), (14, (3, 9), 'W'), (15, (2, 7), 'W'), (12, (4, 3), 'E'), (13, (4, 2), 'E'), (10, (1, 9), 'N'), (11, (1, 5), 'N'), (8, (10, 6), 'N'), (9, (1, 2), 'N'), (6, (6, 6), 'E'), (7, (1, 7), 'N'), (4, (2, 2), 'N'), (3, (5, 3), 'N'), (2, (1, 1), 'N'), (5, (9, 10), 'E'), (6, (9, 2), 'W'), (4, (9, 1), 'E'), (2, (10, 3), 'N')],
    [(1, (5, 2), 'N'), (23, (8, 9), 'W'), (22, (8, 2), 'W'), (21, (8, 5), 'W'), (20, (5, 8), 'W'), (19, (7, 4), 'N'), (18, (6, 7), 'N'), (17, (2, 8), 'W'), (16, (2, 6), 'W'), (15, (3, 5), 'W'), (14, (1, 3), 'W'), (13, (7, 2), 'E'), (22, (3, 3), 'S'), (11, (1, 9), 'N'), (8, (10, 7), 'E'), (9, (9, 10), 'E'), (6, (2, 7), 'E'), (7, (2, 5), 'E'), (4, (6, 10), 'E'), (3, (10, 8), 'N'), (2, (8, 8), 'N'), (3, (7, 6), 'N'), (2, (6, 5), 'N'), (7, (9, 4), 'W'), (4, (1, 1), 'N'), (5, (10, 2), 'E'), (5, (10, 1), 'E')],
    [(1, (4, 2), 'N'), (23, (8, 8), 'W'), (22, (8, 2), 'W'), (21, (8, 5), 'W'), (20, (5, 9), 'W'), (19, (7, 3), 'N'), (18, (5, 7), 'N'), (17, (5, 5), 'W'), (16, (1, 6), 'W'), (15, (1, 4), 'W'), (14, (9, 5), 'S'), (9, (10, 10), 'E'), (12, (7, 1), 'E'), (13, (3, 2), 'E'), (8, (5, 1), 'E'), (7, (7, 8), 'E'), (6, (3, 5), 'N'), (5, (9, 9), 'E'), (4, (9, 1), 'E'), (5, (6, 4), 'E'), (2, (7, 5), 'N'), (3, (3, 4), 'N'), (2, (1, 5), 'N'), (3, (10, 7), 'N'), (10, (3, 9), 'N'), (6, (1, 10), 'W'), (4, (2, 8), 'E')],
    [(1, (6, 3), 'N'), (23, (8, 9), 'W'), (22, (7, 3), 'W'), (21, (8, 6), 'W'), (20, (5, 7), 'W'), (19, (9, 5), 'N'), (18, (5, 2), 'N'), (17, (3, 8), 'W'), (16, (1, 8), 'W'), (15, (2, 6), 'W'), (14, (1, 4), 'W'), (13, (8, 10), 'E'), (12, (3, 1), 'E'), (11, (7, 1), 'N'), (10, (4, 5), 'N'), (9, (3, 2), 'N'), (8, (10, 2), 'N'), (7, (1, 6), 'N'), (4, (7, 5), 'N'), (5, (10, 1), 'E'), (4, (4, 3), 'N'), (3, (8, 8), 'N'), (2, (6, 7), 'N'), (3, (6, 1), 'N'), (2, (4, 10), 'N'), (6, (1, 9), 'N')],
    [(1, (4, 7), 'N'), (23, (8, 7), 'W'), (22, (8, 2), 'W'), (21, (8, 3), 'W'), (20, (7, 8), 'W'), (19, (7, 6), 'N'), (18, (4, 5), 'N'), (17, (5, 1), 'W'), (22, (2, 3), 'W'), (15, (5, 9), 'W'), (16, (1, 8), 'W'), (13, (7, 4), 'E'), (14, (1, 6), 'W'), (11, (2, 1), 'N'), (8, (10, 10), 'E'), (9, (1, 3), 'N'), (6, (5, 6), 'N'), (5, (3, 6), 'N'), (4, (1, 1), 'N'), (3, (10, 9), 'N'), (2, (8, 8), 'N'), (3, (7, 10), 'N'), (2, (6, 5), 'N'), (7, (9, 2), 'W'), (6, (1, 9), 'N'), (7, (10, 6), 'S'), (5, (9, 1), 'E')],
    [(1, (3, 1), 'N'), (23, (8, 8), 'W'), (22, (8, 3), 'W'), (21, (8, 5), 'W'), (20, (5, 9), 'W'), (19, (7, 4), 'N'), (18, (6, 2), 'N'), (17, (5, 6), 'W'), (16, (4, 7), 'W'), (15, (3, 9), 'W'), (14, (4, 4), 'W'), (13, (10, 10), 'E'), (12, (4, 6), 'E'), (11, (1, 9), 'N'), (10, (1, 5), 'N'), (9, (10, 1), 'E'), (8, (1, 2), 'N'), (7, (1, 7), 'N'), (4, (4, 5), 'E'), (5, (9, 2), 'E'), (2, (10, 4), 'N'), (3, (9, 5), 'N'), (2, (8, 10), 'N'), (3, (8, 7), 'N'), (6, (3, 3), 'W'), (6, (2, 2), 'W'), (4, (5, 1), 'E')]
    
    ]
evaluationTestGameLabels = [
    100,
    101,    
    101,
    101,
    100,
    101,
    100,
    100,
    101,
    100
    ]

pRl15 = []
rcRl15 = []


def raw(game):
    data = []
    for i in range(0,144):
        if (i%12 == 0 or i%12 == 11) or i < 12 or i > 131:
            continue
        data.append(game.board[i])
    return data

def getScore(clf, l, p):
    totalScore = 0
    c = 0
    s = 0
    for moves, winner in zip(evaluationTestGames, evaluationTestGameLabels):
        if s < 4:
            s+=1
            continue
       
        game = Cathedral()
        score = 0
        for move in moves:
            game.placePiece(move[0], move[1], move[2])
            
            playerIndex = list(clf.classes_).index(winner)
            prob = clf.predict_proba([raw(game)])
            
            totalScore += prob[0][playerIndex]
            c+=1
            l.append(winner == Cathedral.lightPlayer)
            p.append(clf.classes_[np.argmax(prob[0])] == Cathedral.lightPlayer)
            
    return totalScore / c

#RL - 10 nodes
reinforcementLearningResults10 = []

pickleNames = os.listdir(path.join(thisPath,'RL', 'pickles'))
sortedPickles = sorted(pickleNames,reverse=False)
for model in sortedPickles:
    l = []
    p = []
    clf = load(path.join(thisPath, 'RL','pickles', model))
    reinforcementLearningResults10.append(getScore(clf, l,p))
   

#RL - 15 nodes
reinforcementLearningResults15 = []

pickleNames = os.listdir(path.join(thisPath, 'pickles'))
sortedPickles = sorted(pickleNames,reverse=False)
for model in sortedPickles:
    l = []
    p = []
    clf = load(path.join(thisPath, 'pickles', model))
    reinforcementLearningResults15.append(getScore(clf, l,p))
    pRl15.append(pre(l,p, average='binary'))
    rcRl15.append(rc(l,p, average='binary'))
    

#SL - 10 nodes
supervisedLearningResults10 = []

pickleNames = os.listdir(path.join(thisPath, 'sl-pickles-10'))
sortedPickles = sorted(pickleNames,reverse=False)
for model in sortedPickles:
    l = []
    p = []
    clf = load(path.join(thisPath, 'sl-pickles-10', model))
    supervisedLearningResults10.append(getScore(clf, l,p))
    
#SL - 15 nodes
supervisedLearningResults15 = []

pickleNames = os.listdir(path.join(thisPath, 'sl-pickles-11'))
sortedPickles = sorted(pickleNames,reverse=False)
for model in sortedPickles:
    l = []
    p = []
    clf = load(path.join(thisPath, 'sl-pickles-11', model))
    supervisedLearningResults15.append(getScore(clf, l,p))
  

#Graphs

rl10Xdata = range(5,len(reinforcementLearningResults10)*5+5, 5)

rl15Xdata = range(5,len(reinforcementLearningResults15)*5+5, 5)

sl10Xdata = range(5,len(supervisedLearningResults10)*5+5, 5)

sl15Xdata = range(5,len(supervisedLearningResults15)*5+5, 5)

# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(rl10Xdata, reinforcementLearningResults10, color='tab:blue')

ax.plot(rl15Xdata, reinforcementLearningResults15, color='tab:green')

ax.plot(sl10Xdata, supervisedLearningResults10, color='tab:orange')

ax.plot(sl15Xdata, supervisedLearningResults15, color='tab:red')

# set the limits
ax.set_xlim([5, 5+5*max(len(reinforcementLearningResults10), len(supervisedLearningResults10), len(supervisedLearningResults15), len(reinforcementLearningResults15))])
ax.set_ylim([0, 1.5 * max([max(reinforcementLearningResults10), max(supervisedLearningResults10), max(supervisedLearningResults15), max(reinforcementLearningResults15)]) ])

ax.set_title('Cathedral: Reinforcement V. Supervised Learning')
plt.savefig('4.1.png')

print(pRl15)
print(rcRl15)