[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6175422&assignment_repo_type=AssignmentRepo)
# Object-Based Click Game
A repo for making a SIMPLE object-based game. (PC08 &amp; PC09)

## PC08 - Click Game Pt. 1
In this Programming Challenge, you will practice creating classes and objects to create a simple click game. The game should be as complete as you can make it (please see Requirements and Extra Credit, below). The simplest game is to make bubbles that must be clicked within a certain span of time.
What makes a game?

Your game (and the description at the top of your script) should contain these four elements. Feel free to push the boundaries of these definitions! Ask an LA or Dr. Z if you'd like to exclude one of these elements in your game.

    Objective - what needs to be accomplished to complete a level or beat the game
    Rules - What can and cannot happen in meeting the objective, usually relates to timing or scoring if applicable
    Challenge - A procedure, action, confrontation or difficulty the player must enact in order to achieve the objective
    Interactions - how the player, enemy and/or environment affect each other

Key terms:

    The user - the human (or computer!) who is controlling the game play.
    The player - the game representation of the user

Games will always have users, but may not have players!

**Examples:**

**[Bellwoods](http://bellwoods.xyz/)**

    Objective - find a colored circle in the woods that has not yet been found. Collect birds as you advance!
    Rules - the user can click and drag the kite to move it around the woods. 
    Challenge - the player can only see a small view of the woods at a time. The circle can be anywhere!
    Interactions - as the player move the kite through the woods, they play peaceful bell sounds. The birds will indicate the level, with the newest bird directing the player to the next circle

**[Space Invaders](https://www.andoverpatio.co.uk/21/space-invaders/)** 

    Objective - prevent descending aliens from reaching the bottom of the screen
    Rules - shoot aliens with a blaster to collect points -- different aliens have different point values. Use the blockades to hide from alien blasts
    Challenge - the player can only pan left and right on the screen (not up and down). Aliens shoot back. Aliens move faster as they get closer to the bottom of the screen. The "mothership" moves quickly and cannot be attacked until the end.
    Interactions - the player can destroy aliens by shooting them, if an alien touches the blaster, the game is over. If the player gets shot by an alien, the game is over. Both player and alien can destroy the blockades.

 
## Requirements:
1. **Pseudocode** describing game look, rules, objectives and at least 1 end condition (win or lose). **Submit with .py on Nov 3rd**
2. Create **at least 1 class** to generate objects that have a movement and/or click behavior that get incorporated into game play. Classes should include:
    a. the init() method with at least 2 parameters
    b. a second method (such as one to be used with onclick)
3. More than one object should be instantiated, with different arguments (such as varying positions or colors)
4. **Any image or sound files that are used must be submitted with the script (.py) or you will lose points!**
5. **At least 1 end condition** (did you user win or did they lose lose) must occur. Print statements are fine.
6. Be sure to follow good code quality, including a description that details:
        The rules and objectives of the game
        Basic how-to-play instructions ("use your mouse to..", "navigate with..")
7. *(Optional)* You can consider making a second class that creates & controls a countdown timer. An example of a countdown timer (not in a class) can be found in the Class Code Repository (linked below).

 
## What's too much?
1. Having levels where the entire scene gets redrawn/reset is difficult. Changing background color/theme color (a la Bellwoods) is easier.
2. Baddies as inherited classes from good guys. If you don't now what this sentence means, you probably shouldn't tackle this. You can make baddies from a separate class. I strongly recommend making a complete game with good components first *then* try to add baddies.
3. Sound effects can be tricky. See the randoTurtOOP.py example in the Class Code Repo for examples.
4. Collision detection can be challenging but it is doable. There is example code in the Class Code Repo. I recommend staying away from maze games at this point.

Class Code Repo linked in Resources.
 
## Resources:

**[USE THE DOCS! USE THE DOCS! USE THE DOCS! (Have them open while you code.)](https://docs.python.org/3/library/turtle.html)**

- The write() method will be particularly of use in this Challenge. Writing text with turtles [(interactive example)](https://trinket.io/python/52378ec006).
- [Multiple objects](https://canvas.colorado.edu/courses/75648/pages/multiple-objects-working-with-lists) - Tips on working with lists of objects
- Interested in using different (sound) libraries? Here's how to install them. In the command line type:
    `pip install <module name>`
- [Class Code repository](https://github.com/ATLS1300/Class-Code/) - useful code and examples. Only borrow/use what you understand! You may get points withheld until questions about borrowed code get answered.

 
## Extra Credit (Grads must complete at least 2):

0.5 pt - create a 2nd class that controls a 2nd component of the game (countdown, score keeping, etc)

0.5 pts - incorporate key press (hint: use the turtle docs, startBubble.py in the Class Code Repo has an example, too)

0.5 pts - share or show your game with/to a friend, and have them give you feedback (included in comments). They should comment on how fun it was, what they liked and what could be improved.

1 pt - [inherit](https://books.trinket.io/pfe/14-objects.html#inheritance) the Turtle class into your class for more streamlined class construction. (Hint: you will need to call the super init method: super().__init__())

1 pt - Use and animate a list of objects.

2 pts - Tailor this game for an underserved audience (elderly, incarcerated, illiterate, disabled, neurodiverse, low-income, etc). In the description, describe who this is for and how you adapted your game for them. Links to research encouraged.
