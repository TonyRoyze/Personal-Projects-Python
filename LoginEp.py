import pyperclip
import sys

pyperclip.copy(f"document.getElementById('login_email').value = '{sys.argv[3].lower()}';\ndocument.getElementById('login_password').value = '{sys.argv[4]}';")
