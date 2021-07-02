#!/usr/bin/python3.9

#How to run
#in the command line go to the directory of the file and type ./mapIt.py address
#you can type an address or copy an address(and leave the address spot blank)
# then a page should pop up with google maps and the address

import webbrowser, sys, pyperclip

# webbrowser.open('https://inventwithpython.com/')
# address 5175 E Clinton Way, Fresno, CA 93727

# checks for address enterd
if len(sys.argv) > 1 :
    find = '+'.join(sys.argv[1:])
else:#if len(sys.argv) == 1: #if no address
    find = pyperclip.paste().replace(' ', '+') #puts string in correct format
    
url = f"https://www.google.com/maps/place/{find}" #google maps url

webbrowser.open(url) #opens web page
