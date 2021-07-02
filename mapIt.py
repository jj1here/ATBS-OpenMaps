#!/usr/bin/python3.9

import webbrowser, sys, pyperclip

# webbrowser.open('https://inventwithpython.com/')

if len(sys.argv) > 1 :
    find = '+'.join(sys.argv[1:])
else:#if len(sys.argv) == 1:
    find = pyperclip.paste().replace(' ', '+').replace(',','')
    
url = f"https://www.google.com/maps/place/{find}"

webbrowser.open(url)
