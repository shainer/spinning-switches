# Spinning switches

The spinning switches problem has been taken from the book of mathematical puzzles **So you think you've got problems?** by Alex Bellos.

There are two spinning switches problems in the book; we are going to focus on the second, or most advanced, formulation.

## The problem

You are locked inside a cell. On the door, there is a wheel with four switches, arranged around the wheel. You can imagine each switch located at one of the cardinal directions (north, west, south and east). At the beginning, each switch can be in either the **on** or **off** position at random, but you are not able to see their current state. The door will unlock once all four of them are on the **on** position.

At each stage, you can flip any combination of switches (1, 2, 3 or all of them). If your operation results in all switches going to the **on** position, the door unlocks and you win the game. If your operation does not result in victory, the wheel with the switches will randomly rotate; after this, you can no longer locate the current position of any switch.

What is the sequence of operations that guarantees you will always unlock the door, regardless of the starting states of the switches? You have no upper bound on the number of operations you can perform.

## This program

This program implements the game, and runs through the sequence of actions that is guaranteed to win. Continue reading for an explanation of why that is the winning strategy.

## The winning strategy

First, some naming convention. Here are the possible actions and the names I assigned them in the code:

- **ALL**: press all 4 switches;
- **THREE**: press 3 random switches;
- **OPP**: press 2 opposite switches. Remember that even if we implement the switches as a list, in the original problem they are arranged around a wheel, so this makes sense;
- **ADJ**: press 2 adjacent switches (see above).
- **ONE**: press 1 switch.

I started by listing all possible state transitions. If you start from state X, and apply action Y, which next states can result?

Example: if I have 1 switch on, and I do action **THREE**, I have two possible next states: victory (I turned on all the off switches) or 2 switches on (I turned off the one ON switch and turned on two random OFF switches).

Note that when you do the above, since switches randomly rotate around with every wrong action, you cannot make any assumption about which switches you press compared to those in a given state. You have to spell out your transition considering all possible cases.

Then, note that the wheel rotates after each incorrect action, which means that the switches move around (to confuse you) but never change their position relative to one another. If you end up in the state "2 adjacent switches are on", that state is persisted after the rotation.

Looking at all the actions and their transitions we will discover how to progressively "exclude" each possible starting state. We exclude a state by performing an action that either makes us win, or brings us to a different, well-known state (ideally only 1).

The first interesting transition happens with action **ALL**: if all switches were off, then I won. Otherwise, I've just reversed all switches. This means that any time I suspect I might be in the "all switches off" position, I should add one **ALL** action to my sequence, and effectively exclude that state.

So I am going to start by doing exactly that. My first action is **ALL**; if I am lucky, I've won already, otherwise I was in another state (1, 2 or 3 switches on) and I am now in a different state of that same list.

The second interesting transition becomes noticeable when I look at the decision table for the **OPP** action. I'll write it down here.

- 1 switch on -> 3 on OR 1 on;
- 3 switches on -> 3 on OR 1 on;
- 2 adjacent switches on -> no change;
- 2 opposite switches on -> all off, or victory.

Note that having excluded the "0 switches off" state at the previous step, I don't need to list it here.

Interesting. This means that if I add an **OPP** action, followed by another **ALL** action, I've either won the game, or effectively excluded the "2 opposite switches" starting state as a possibility. Assuming I haven't won yet, I am now in one of these possible states: 1 switch on, 3 switches on, 2 adjacent switches on.

Let's look at the **ADJ** transition for these states:

- 1 switch on -> 3 on or 1 on;
- 3 switches on -> 3 on or 1 on;
- 2 adjacent switches on -> 2 opposite switches on, victory or all off.

If I am in the "2 adjacent switches on" state, the **ADJ** action moves me to a bunch of states I already know to exclude. I can win immediately, win after another **ALL** action, or I was in the "2 opposite switches on" state, which I know how to exclude.

My sequence becomes the following:

```
ALL OPP ALL ADJ ALL OPP ALL
```

Now I have two remaining possible initial states to tackle: 1 switch on and 3 switches on. This is more convoluted because now, the "wrong" move can take me back to one of the "2 switches on" state. There isn't really a way to avoid this.

Looking again at the decision tables, the best action is **ONE**. Here's what happens:

- 1 switch on -> all off, or 2 switches on (either opposite or adjacent);
- 3 switches on -> victory or 2 switches on (either opposite or adjacent);

This action is promising because it's the only one that does not let me transition between the 1 state and the 3 state (or viceversa). I am always moving to other states, which I know how to handle.

The possible transitions in practice are: I win immediately, I win after another **ALL** action, or I need to repeat the whole sequence we've built so far to get out of one of the "2 switches on" states (I do't know which one, so I need to repeat the entire thing).

```
ONE ALL ALL OPP ALL ADJ ALL OPP ALL
```

And here we go! You can see the full sequence in the code, and you can run it as many times as you want to convince yourself that you will eventually win any game.