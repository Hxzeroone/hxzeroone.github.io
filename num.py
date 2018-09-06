# -*- coding: utf-8 -*-
#please donot steal the credits.
import urllib2
#banner
banner="""
###################################
#┬┌┐┌┌─┐┌─┐  ┌─┐┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐#
#││││├┤ │ │  │  ├─┤├┤ │  ├┴┐├┤ ├┬┘#
#┴┘└┘└  └─┘  └─┘┴ ┴└─┘└─┘┴ ┴└─┘┴└─#
###################################
"""
#colors
class bcolors:
             RED = '\033[91m'
             YELL = '\033[93m'
             BOLD = '\033[1m'

print ( bcolors.BOLD + bcolors.YELL + banner + bcolors.RED)
#userinput
phone = raw_input(bcolors.BOLD +"[+] Enter Phone Number Without 0 :"+ bcolors.YELL)
print ("[+] Inf0 :")
#req
inf = urllib2.urlopen('https://c4u.000webhostapp.com/ahtest/api.php?number='+phone).read( )
#use web gui :https://c4u.000webhostapp.com/ahtest/
print inf
