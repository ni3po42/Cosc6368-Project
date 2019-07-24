from mctspy.tree.nodes import TwoPlayersGameMonteCarloTreeSearchNode
import numpy as np
import time

class NeuralNetNode(TwoPlayersGameMonteCarloTreeSearchNode):

    def __init__(self, state, clf, parent=None, oneSided=None):
        super().__init__(state, parent)
        self.clf = clf
        self.oneSided = oneSided
    # def best_child(self, c_param=1.4):
    #     choices_weights = [
    #         (c.q / c.n) + c_param * np.sqrt((2 * np.log(self.n) / c.n))
    #         for c in self.children
    #     ]
    #     return self.children[np.argmax(choices_weights)]

    def expand(self):
        action = self.untried_actions.pop()
        next_state = self.state.move(action)
        child_node = NeuralNetNode(
            next_state, self.clf, parent=self, oneSided=self.oneSided
        )
        self.children.append(child_node)
        return child_node

    def rollout_policy(self, possible_moves):    
        if self.clf is None or self.oneSided is None or self.oneSided != self.state.next_to_move:
            # initial random for learning
           # start = time.time()
            index = np.random.randint(len(possible_moves))
        #    end = time.time()
         #   print ("rando time: ", end - start)
            return possible_moves[index]
        else:
            
            #start = time.time()
            
            p = [ self.state.raw(possible_move) for possible_move in possible_moves]
            
            playerIndex = list(self.clf.classes_).index(self.state.next_to_move)
            
            
            predictions = [ v[playerIndex] for v in self.clf.predict_proba(p)]
            
            index = np.argmax(predictions)
            
            #end = time.time()
            #print ("prediction time: ", end - start)
            #print ('index: ', index, 'pred_prob: ', predictions[index], 'move: ' ,possible_moves[index])
            
            return possible_moves[index]