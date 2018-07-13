import requests,re,json
from bs4 import BeautifulSoup
from decimal import Decimal

number = input("Enter Phone Number: ")

def number_info(number):
    try:
        page = requests.get('https://carbonmonoxide2.000webhostapp.com/api.php?num=' + number)
        s = BeautifulSoup(page.text, 'html.parser')
        if s.get_text() == '[]':
            print("[-]Number Not Found!")
        else:
            print(json.dumps(json.loads(s.get_text()), indent=1).translate ({ord(c): " " for c in '()[]{}",'}))         #    rx = re.sub(r'[?|$|.|!|{}|""|]',r'',soup.get_text()).strip('[]').replace(',', '\n').replace(':', ':  ').replace('/', '')
    except:
        print("Something went wrong!")
number_info(number)
