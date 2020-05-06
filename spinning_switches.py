#!/usr/bin/python3

import random

NUM_SWITCHES = 4
# Sequence of actions guaranteed to win every game.
ACTIONS = ["ALL", "OPP", "ALL", "ADJ", "ALL", "OPP", "ALL", "ONE", "ALL", "ALL", "OPP", "ALL", "ADJ", "ALL", "OPP", "ALL"]

def randomInitialValue():
    return bool(random.randint(0, 1))
    
def victoryCondition(switches):
    return all(switches)
    
def randomSpinning(switches):
    """Randomly spins the switches (applies random translation of elements)."""
    step = random.randint(0, NUM_SWITCHES-1)
    spinned = []

    for i in range(len(switches)):
        spinned.append(switches[(i + step) % len(switches)])

    return spinned
    
def flipAllSwitches(switches):
    print("ALL: Flipping all switches")
    return [not s for s in switches]

def flipOneSwitch(switches):
    print("ONE: Flipping one switch")

    pos = random.randint(0, NUM_SWITCHES-1)
    flipped = []
    for i in range(len(switches)):
        if i == pos:
            flipped.append(not switches[i])
        else:
            flipped.append(switches[i])
    return flipped

def flipThreeSwitches(switches):
    print("THREE: Flipping three switches")

    # Random selection of three distinct switches.
    positions = random.sample(range(0, NUM_SWITCHES), 3)

    flipped = []
    for i in range(len(switches)):
        if i in positions:
            flipped.append(not switches[i])
        else:
            flipped.append(switches[i])
    return flipped

def flipTwoAdjacent(switches):
    print("ADJ: Flipping two adjacent switches")
    pos1 = random.randint(0, NUM_SWITCHES-1)

    # Randomly decide which adjacent switch is flipped.
    left = (pos1 - 1) if pos1 != 0 else NUM_SWITCHES-1
    right = (pos1 + 1) % NUM_SWITCHES

    pos2 = random.choice([left, right])
    flipped = []

    for i in range(len(switches)):
        if i == pos1 or i == pos2:
            flipped.append(not switches[i])
        else:
            flipped.append(switches[i])
    return flipped

def flipTwoOpposite(switches):
    print("OPP: Flipping two opposite switches")
    pos1 = random.randint(0, NUM_SWITCHES-1)
    pos2 = (pos1 + 2) % NUM_SWITCHES
    flipped = []

    for i in range(len(switches)):
        if i == pos1 or i == pos2:
            flipped.append(not switches[i])
        else:
            flipped.append(switches[i])
    return flipped

def newGame():
    initial_switches = []
    for _ in range(NUM_SWITCHES):
        initial_switches.append(randomInitialValue())
    switches = initial_switches

    if victoryCondition(switches):
        print("Initial victory!")
        return

    for a in ACTIONS:
        print("[**]", str(switches))

        if a == "ALL":
            switches = flipAllSwitches(switches)
        elif a == "OPP":
            switches = flipTwoOpposite(switches)
        elif a == "ADJ":
            switches = flipTwoAdjacent(switches)
        elif a == "ONE":
            switches = flipOneSwitch(switches)
        elif a == "THREE":
            switches = flipThreeSwitches(switches)
        else:
            print("Unrecognized action:", a)
            return
            
        if victoryCondition(switches):
            print("[**] Congratulations! The initial combination was", str(initial_switches))
            return
        else:
            print("(Pre-spinning)", str(switches))
            switches = randomSpinning(switches)
    
    print("You ran out of actions, but no victory in sight... The initial combination was", str(initial_switches))
    return


if __name__ == '__main__':
    newGame()
