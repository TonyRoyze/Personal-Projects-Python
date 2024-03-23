import pyperclip
import sys

pyperclip.copy(f"document.getElementsByClassName('input--style-4')[0].value='{sys.argv[1].title()}';\ndocument.getElementsByClassName('input--style-4')[1].value='{sys.argv[2].title()}';\ndocument.getElementsByClassName('input--style-4')[2].value='{sys.argv[3].lower()}';\ndocument.getElementsByClassName('input--style-4')[3].value='{sys.argv[4]}';\ndocument.getElementsByClassName('input--style-4')[4].value='0{sys.argv[5]}';")
