# Python Terminal Super Mario

There are no dependencies. Important to note that the game has been tested on **ONLY** Linux-based OSs, and _may not_ work on Windows.

## Structure
The application demonstrates inheritance, encapsulation, polymorphism and abstraction.
- Each "object" is a derived class of the `Object` class.
- Each player/enemy is a derived class of the `Person` class.
- The `board` has its own class and and captures all objects placed on it.

## Running the program
- First, install all the requirements:
	- `pip install -r requirements.txt`
- Running the game is easy
    - `python3 main.py`

## Controls
- Controls follow traditional classic titles (W,A,D)
- To quit, press `q`

## File Structure
.
├── board.py
├── conf.py
├── main.py
├── objects.py
├── people.py
├── README.md
└── requirements.txt

## Features
- The name of my mario is bond.
- There are 3 lives, whenever a life is lost, game starts from the beginning.
- Bricks-
    * '[]' normal brick that breaks.
    * 'oo' Mario gets bigger hitting it twice.
    * '??' Brick that has 10 coins , on hitting it changes to 'xx'
- Enemies-
    * 'EE' normal enemies that move left, right
    * 'UU' touching them will kill mario
    * 'SS' smart enemies that follow the mario
    * Boss enemy at the end, that can fire
- Pits - Mario dies by falling in the pit
- Spring - on landing on spring mario jumps double than normal
- Coins
- Pipe
- Badal - Kyunki badal important hai Babu!

## Scoring system
- Killing enemies gives points.
- Breaking a brick gives points.
- Scores for collecting coins.
