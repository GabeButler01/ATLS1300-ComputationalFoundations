[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5513489&assignment_repo_type=AssignmentRepo)
# PC02-Graffiti - Read thoroughly before starting!
<br>
To get started on this assignment, download or clone the files in this repository. To do so:<br>
1. Click the green button above <br>
2. Select "Download ZIP". <br>
3. Unzip the downloaded file and place the created folder into the folder for this class that you have on your computer.
<br>
<br>

## The Assignment
1. Practice drawing using turtle's navigation and pixel locations.
2. Practice drawing shapes and lines. 
3. Explore the turtle library functions.
4. Create some art! (Graffiti is art, you know.)

You'll use the **turtle library** to modify an image using the code snippets we built during the week.

Download this starter repository. In it, you'll find a starter code and this picture of JEFF BEZOS (below). The start code already loads in the image of JEFF BEZOS to your turtle panel. On this image, you may draw whatever you like--positive or negative or whacky imagery. Please keep content appropriate.

![Jeff Bezos](https://github.com/ATLS1300/PC02-Graffiti/blob/image?raw=true)

>Jeff Bezos is the CEO of Amazon, recently reported to have a net worth of $200 billion dollars (that's: $200,000,000,000,000, or the GDP of Kentucky), making him the richest human in history. Bezos has made $86 billion dollars since the start of COVID-19 measures, and has the equivalent wealth of 2.3 million US residents.

>To draw on Jeff Bezos, you may have to move your turtle to different pixel locations. A pixel, short for **pic**ture **el**ement, is the smallest unit of a picture. Most screens have upwards of 1000 pixels in its longest dimension. To get a sense of what pixels are and how right Jeff Bezos is, check out this [data visualization](https://mkorostoff.github.io/1-pixel-wealth/).

## The start code

The start code has some code written for you. This is to help you get started quickly. 
The start code sets the drawing window to 750 x 750 pixels, meaning you have 750 pixels horizontally (x), and 750 pixels vertically (y). Remember, the origin (0,0) is at the **center of the picture**, so to move to the righthand edge, your turtle moves forward 375 pixels, and to the lefthand edge, you'd move -375 pixels. Upward movement is positive, and downward movement is negative. The syntax to move your turtle is shown below.

```forward(375)```

## Your task

To this image, add **at least 2 different geometric shapes** - a circle, a polygon (+4 sides), and a line

For full credit, these shapes must:
    1. have different weights (or thicknesses) of the lines
    2. be drawn at different positions on the screen 
    (Hint: to navigate your turtle, you can use ```goto(x,y)``` for a specific position, or pick up the pen ```up()``` and use ```forward()``` and turns (```left()```, ```right()```).

## HOW YOU SHOULD SPEND RECITATION:

1. Play!


   - Explore using the [Turtle Library documentation](https://docs.python.org/3/library/turtle.html#turtle.forward) and the code that we made in class to see what turtle can do! There's no wrong way to code, this is your expression. Play with colors, shapes, and look up commands. 
   - Here are of all the [string color names in the turtle library](https://cs111.wellesley.edu/labs/lab01/colors) (to use with ```pencolor()``` or ```color()```)
   - Use the **command line** to try different commands. When you find a command you like, paste it into the **text editor**.
       - To save your work, you must add your lines to the text editor! Running your code autosaves it. Run your code often!

2. Sketch!

   - Now that you know what to do with turtle, sketch some things out! You can write notes to yourself, or make an actual drawing. Note where and how you'll change color, shapes and pen width.

3. Test your code!

   - You'll be working between the command line and text editor. Make sure you run your code (green play button) to make sure it does what you want BEFORE you turn it in!

## EXTRA CREDIT - Grad students _must_ complete at least 2!

    0.5 pts - create a 3rd shape

    0.5 pts - set at least one color using RGB values. 

    0.5 pts - create one unfilled and one filled shape

 
## For full credit 

Save your .py file as:

    PC02_Graffiti.py

*Note: This class uses **autograders** -- code that looks for requirements. This kind of test code is an industry standard, so we'll get you used to working with them! This also means failure to name files and following instructions exactly may result in a point deduction! Check your spelling & check your requirements! *

Submit through Github Classrooms by uploading the file into **this repository**. 


