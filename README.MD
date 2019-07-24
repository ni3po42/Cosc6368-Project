Source Code for Timothy Stratton's Cosc6368 Summer project

Game code:
cathedral.py - define rules for game

Game unit tests:
cathedral_test.py - tests to confirm game rules valid
runTests.sh - script for running tests

MCTS code:
cathedralstate.py - wrapper for game to run in MCTS library
neuralnetnode.py - extended from TwoPlayersGameMonteCarloTreeSearchNode to change rollout policy to use a MLPClassifier

