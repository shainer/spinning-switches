# Spinning switches

The spinning switches problem has been taken from the book of mathematical puzzles **So you think you've got problems?** by Alex Bellos.

There are two spinning switches problems in the book; we are going to focus on the second, or most advanced, formulation.

## The problem

You are locked inside a cell. On the door, there is a wheel with four switches; at the beginning, each switch can be in either the **on** or **off** position at random, but you are not able to see their current state. The door will unlock once all four of them are on the **on** position.

At each stage, you can flip any combination of switches (1, 2, 3 or all of them). If your operation results in all switches going to the **on** position, the door unlocks and you win the game. If your operation does not result in victory, the wheel with the switches will randomly rotate; after this, you can no longer locate the current position of any switch.

What is the sequence of operations that guarantees you will always unlock the door, regardless of the starting states of the switches? You have no upper bound on the number of operations you can perform.

## This program

This program implements the game, and runs through the sequence of actions that is guaranteed to win. Continue reading for an explanation of why that is the winning strategy.

## The winning strategy

TBD
