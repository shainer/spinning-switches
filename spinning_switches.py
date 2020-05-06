#!/usr/bin/python3

import random

ACTIONS = []

def randomInitialValue():
    return random.randint(0, 1)
    
    
def victoryCondition(switches):
    return all(switch == 1 for switch in switches)
    
def randomSpinning(switches):
    step = random.randint(0, 3)
    
def flipAllSwitches(switches):
    flippedSwitches = []
    

def newGame():
    initial_switches = [randomInitialValue()] * 4
    switches = initial_switches

    if victoryCondition(switches):
        print("Initial victory!")
        return

    for a in ACTIONS:
        if a == 'ALL':
            switches = flipAllSwitches(switches)
        elif a == 'OPP':
            switches = flipTwoOpposite(switches)
        elif a == 'ADJ':
            switches = flipTwoAdjacents(switches)
        elif a == 'ONE':
            switches = flipOneSwitch(switches)
        elif a == 'THREE':
            switches = flipThreeSwitches(switches)
        else:
            print("Unrecognized action %s" % a)
            return
            
        if victoryCondition(switches):
            print("Congratulations! The initial combination was: %s" % str(initial_switches))
            return
        else:
            switches = randomSpinning(switches)
    
    print("You ran out of actions, but no victory in sight... The initial combination was: %s" % str(initial_switches))
    return


if __name__ == '__main__':
    newGame()
