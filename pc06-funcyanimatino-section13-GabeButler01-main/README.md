[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5904894&assignment_repo_type=AssignmentRepo)
# PC06-Funcy-Animation
We're starting to move toward task-oriented programming--making code that uses almost entirely functions to execute a task. This will help us build toward Object Oriented Programming (OOP) which is the culmination of this course's learning goals. Scary, right? #hallowee!

### In this repo
1. **img2gif.py** - Python turtle only works with .gif files. (Changing the extension or converting it in Adobe won't work.) To use this tool, download and place the file in the same folder as the image of choice. Read the code description carefully, and interact with the code in the command line console.
2. **start_code.py** - Start code with commented sections to help your code organization. There are also some key changes to turtle! Including: <br>
        `turtle.tracer(0)` this command turns off turtle's built-in animation, but requires the panel to be updated manually.<br>
        `panel.update()` this command updates the information sent to draw on the panel. This should be called at the end of a frame drawing (end of while loop block)<br>
        `running = True` this boolean variable is used to control the animation loop. To have stop conditions, you should use a conditional statement inside of the loop to change the value of running from `True` to `False`.
3. **wrapAroundBoundary.py** - Example code demonstrating how while loops are used to make animations, how conditional statements can be used for edge detection.

## Work smart!

**Protips**: 
- Consider using code you've already created in this class. Build the pattern from PC03 or reuse the code from PC04 to make a cool pattern that moves or has some fun behavior. <br>
- Behaviors do not have to be repetitive! They can wiggle, bounce, spin, get bigger or smaller, hide behind objects...
- Image/object collision is **HARD** Keep it simple and plan to build on it as you learn!
- You do not have to build your code following the organization described with comments. Build how you best work, then clean up afterward. 
- Restart your kernel and run your code to make sure it works! 
- **Submit your images with your files!!**

**Use the Net**
As you are expending your skillset, you should consider looking to see if the solution you need exists already. Use search engines to search for:<br>
    `python turtle` plus whatever the rest of your description is.<br>
This means you'll get practice articulating and describing what you want your code to do!

### Remember to cite code and use no more than 20% of borrowed code
`# code modified from <URL>`<br>
`# code borrowed from <URL>`

There is also a [repository of useful code](https://github.com/ATLS1300/EasyExamples) for you to use. The 20% limit does not apply to this code, **but you must cite it**. Check back frequently, as it will regularly be updated (based on student requests)!

## The Assignment
Using the start_code.py in the repo, create an animation that is function based. You can do this 1 of 2 ways:

1. (Medium difficulty) Call the function inside of the while loop like so:

`running = Tru`e<br>
`while running:`<br>
 `   someFunction()`

2. (Hard difficulty) Put the while loop inside of the function definition, so when it calls, it free-runs the animation.

`def **someFunction**(step):`<br>
 `   while running:`<br>
 `       turtle.forward(step)`<br>
`...`<br>
`someFunction() # runs the whole shebang`

Create an engaging and enticing animation. Consider:
- using multiple turtles to draw complex patterns
- storytelling--parables, memes and short stories are great inspirations
- color, speed and textures to evoke moods and sensations
- simple, high contrast linear movements can be very engaging!

## Requirements
Your assignment must: <br>
    1. Have one unique function that is both defined and called. (Please don't borrow a function if you can help it...the point is practice.)<br>
    2. At least one function must be called within the animation loop (while loop) <br>
    3. **Include any images you used in your code!**
    
### Extra Credit (Grads must complete 2)
    - 0.5 pts - use an image for the turtle shape
    - 0.5 pts - have a conditional statement that stops the while loop (change the value of the variable `running` to `False`)
    - 1 pt - if using a <=3 turtles, try using them in a list!
    - 1 pts - create a function that returns a boolean for any edge detection (remember descriptive naming!)

## Submit to this repository:
    - MP04 - your edited version of wrapAroundBoundary.py
    - PC06 - your pseudocode for your animation
    - PC06 - your script (.py file)
    - PC06 - any images you used in your code!
    
### MP04 Due Fri
### PC06 Pseudocode Due Sun
### PC06 Due Weds
