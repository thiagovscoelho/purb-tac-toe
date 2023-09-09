# purb-tac-toe

Implements console-based gameplay of the Purb variant of tic-tac-toe against a computer that chooses moves randomly.

## Origin of the game

purb and inure [have sent each other](https://twitter.com/purrblind1/status/1700305986723139694) these text messages:

inure:
    x

purb:
    x o

inure:
    x o
      x

purb:
    x o
      x
        o

inure:
    x o
      x
    x   o

purb:
    x o o
      x
    x   o

purb:
    wait

inure:
    x o o
    x x
    x   o

inure:
    I win

purb:
    NOOOOOOOOOOOOOOOOO

The messages consist in a form of tic-tac-toe played via text. However, the interesting fact is that the first few messages started out with a 1x1, then 2x2 grid, which was “expanded” up to 3x3 as new moves required it. This represents a new, unsolved variant of tic-tac-toe.

## How it is played

You play as purb, who has now decided to play the game against yummi, the computer. Since yummi is only a cat, he chooses moves randomly. When yummi plays, he helpfully gives you numbers and letters that you can type to choose where you’ll place your move. Given the structure of the game as played by purb and inure, there are many choices early on, but the board quickly settles onto its normal 3x3 size and stays that way until the end, which happens, as normal, with either a win from one of the sides or a “cat’s game”, which is a tie. (It also happens to describe this game anyway, since purb and yummi are both cats.)

The following is an example game.

	yummi:
	1 2 3
	4 x 5
	6 7 8
	purb (enter your move): 6
	purb:
		x  
	  o    
	yummi:
	1 x 2 3
	4 5 x 6
	7 o 8 9
	purb (enter your move): 8
	purb:
	  x    
		x  
	  o o  
	yummi:
	1 x 2
	3 4 x
	x o o
	purb (enter your move): 4
	purb:
	  x  
	  o x
	x o o
	yummi:
	1 x 2
	x o x
	x o o
	purb (enter your move): 1
	purb:
	o x  
	x o x
	x o o
	purb wins!