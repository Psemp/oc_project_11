# project_11

# 1 - Presentation 

This project is meant to be an improvement over the project 3, which goal was to design a small game, a maze in which the player had to get three items, then go 
to the guard and win.
<hr>
Compared to the original project, several improvements have been made : <br>
1. The maze is now generated randomly, so are player and goal positions as well as the objects. A "box" of height*lenght is generated, then a script inserts randomly "blocker" in the matrix. <br>
2. The user can now choose to let the AI solve the Maze, or can solve it himself.
<br>
3. The game now uses Westworld characters and theme, I found it more suited to an AI since the maze in westworld has a strong meaning. Sprites have been modified to match this idea.

# 2 - The AI

The 'AI' uses A* pathfinding algorythm to find the shortest route.
The sortest route is defined by : Start position -> Item -> Item -> Item -> Goal position.
<br>
If the maze is solvable, every possible path is generated (the items can be picked in any order) using permutations from itertools (std lib) - The program then picks, among the generated paths, the shortest. This path is saved and the user can let the AI execute the paths, which is basically a list of tuples.

# 3 - Problems

1. While I tried to program manually A*, it was always kind of flawed, so I used the code from Ryan Collingwood [here](https://gist.github.com/ryancollingwood/32446307e976a11a1185a5394d6657bc). This code uses trigonometry as heuristic while I would have prefered to use manhattan distance to target but I prefered to leave the original A star code untouched.
2. There are inherents problems which are the result of the randomization of the maze generation.
<br>
-> While I have tried my best to avoid the "box" effect (i.e. a floor square surrounded by walls, making it inacessible), it can still appear from time to time. There's a small alert in the CLI informing the user that there was a problem in the maze generation. Just relaunch the program and the error will most likely be gone.
<br>
-> The AI, sometimes, kills itself, this happens when the route to an item overlaps the goal position. Let's say S is start and end is E, I1, I2 and I3 are our items, if, say, E is in path I1 -> I2, the player will lose. This is a rare occurrence but it can happen.


# 4 - Installation

1. Python 3.10
2. python3 -m venv env
3. activate env (source /env/bin/activate <--Mac , env/scripts/activate.ps1 <-- Win)
4. pip3 install -r requirements.txt
5. python3 main.py

