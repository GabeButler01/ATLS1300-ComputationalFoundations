"""
GIF Converter

              THIS SCRIPT MUST GO IN THE SAME FOLDER AS YOUR IMAGES

Dr. Z 
Made: Jan 22, 2020

Modified: Nov 20, 2020 - now allows shrink scaling (removes TypeError for fraction
        scales like 0.5)

This script will prompt users for the name of their file, then convert it to a
.gif and save it. For this script to run properly, the working directory 
(upper right corner) MUST be the same as the file! 

          RUN THE CODE & ANSWER PROMPTS THAT APPEAR IN THE COMMAND LINE ga--->
"""

#modified from https://mail.python.org/pipermail/python-list/2000-May/036017.html
from PIL import Image 
import PIL
import sys, os, ast
os.chdir("/Volumes/Cotyledon/ATLS1300/non-Summer/Fall2020/Class Code")
try:
    name = input("What is the name of the image you'd like to convert? (Please include the extension, no quotes around text!)\n ")
    outputName = name[:name.find('.')] +'.gif' #change name for output

    #do the magic
    img = Image.open(name)
    # transparency = img.info["transparency"]
    decide = input("Do you want to RESIZE this image? (Y/n) ")
    decide2 = input("Do you want to SCALE this image? (keep proportions) (Y/n) ")
    if decide.lower()!='n':
        size = input("Enter your image pixel size as: width,height (in integers please!) "  )
        img = img.resize(ast.literal_eval(size), resample=PIL.Image.BICUBIC)
    elif decide2.lower()!='n':
        scale =float(input("Enter desired scale value. (Ex: 2 will scale twice the size, 0.5 will half it)  \n"))
        img = img.resize((int(img.size[0]*scale), int(img.size[1]*scale)), resample=PIL.Image.BICUBIC)
  
    img.convert('RGB').save(outputName)#, transparency=transparency) #convert to filetype and save
    print('Saved in the current working folder. Have a nice day!')

except FileNotFoundError:
    sys.stdout.write("\033[1;31m" ) #Red
    print( "\nSorry, there's no file by that name.")
    print("Your current working folder is: " + os.getcwd())
    print("Which contains:")
    sys.stdout.write("\033[0;0m") #Black
    print(os.listdir())
    sys.stdout.write("\033[1;34m" ) #Blue
    print("\nPlease check your spelling and working directory, and run this code again!")
    sys.stdout.write("\033[0;0m") #Black
    
    #colors from https://stackoverflow.com/questions/37340049/how-do-i-print-colored-output-to-the-terminal-in-python/37340245