import praw
import os
file = open("password.txt", 'r')
content = file.readlines()
file.close()
i =0
user_agent = "<console:HappyBot:7.0>"
if os.path.isfile('praw.ini'):
	filesize = os.path.getsize("praw.ini")
	if filesize == 0:
	    print('')
	else:
	    file = open('praw.ini', 'w')
	    file.writelines('')
	    file.close()
while i<len(content):
	content[i] = content[i].replace('\n', '')
	i+=1
for con, l in zip(content, range(0, len(content))):
	bot = con.split(':')
	file = open("praw.ini", 'a')
	file.writelines(f"[bot{l}]\nclient_id={bot[2]}\nclient_secret={bot[1]}\npassword={bot[3]}\nusername={bot[0]}\nuser_agent={user_agent}\n\n")
	file.close()