################################
### INSTALL WRECKFEST SERVER ###
################################

Method 1:  
• Open steam, go to library, search for "Wreckfest"
• Install dedicated server

Method 2:
• Download steamcmd - put in it's own directory (simple google search will get you the cmd)
• Open it and let it do it's initial indtallation
• Use the following commands:

login anonymous
force_install_dir <path>
app_update 361580 validate

#########################
### SETTING UP SERVER ###
#########################

In the server directory, make a copy of "initial_server_config.cfg" and name it "server_config.cfg". Open "server_config.cfg" in your preferred text editor (I prefer Notepad++). I have included a "server_config.cfg" in the github if you would like to use that instead.  I have purposefully left out the event loops in that file.

Change at least he following:
• server_name
• welcome_message
• password  (blank if no password)

There really isn't a need to set admins since you can do that right within the server console and the settings will stay.

The general layout of eventloops can be seen in "initial_server_config.cfg" at the bottom.  As you can imagine, doing that for, say, 100 events can be quite tiresome, which is why I made the python script.

#######################
### PORT FORWARDING ###
#######################

Running a dedicated server, you will have to portfoward the following ports:

• UDP 27015
• UDP 27016
• UDP 33540
• TCP 27015

If you don't know how to portforward, go to https://www.portforward.com

#######################
### TEST CONNECTION ###
#######################

Once all of the above is complete, run the file "start_server.bat".  You'll get a windows firewall prompt and allow whatever it is asking, otherwise you won't get a connection.

The prompt will go through a series of initializations and once you see "Starting server..." and then "Server connected to Steam." you should, in theory, be good to go.  Log into wreckfest, go to multiplayer, then LAN tab and you should see your server.  If you don't, the only thing I can recommend is checking your portforwards and if that doesn't work, reinstalling the server through steam.  I'm not going to add a troubleshooting server guide.

#####################
### SETTING ADMIN ###
#####################

Once the server is up, pressing [ENTER] will give you a list of commands.

• Any command beginning with "/" can be done from within the game lobby by an admins
• Any commmand that does not begin with "/" must be done through the server's command line.

The easiest way to set admin is to launch wreckfest and join the server.  Once in, use the following commands:

• bots 0 		# this gets ride of any bots in the server
• list			# lists the players connected, take note of your id  "1: <steam name>"
• /admin [id]	# this will give you admin and the server will keep that as long as "clear_users=0" in "server_config.cfg"

From here, your server is functional.  There is no eventloop set, but you can change settings per map just like you were hosting it through the game.  The next steps will show you how to populate the eventloop at the bottom of the script.

###NOTE: I do not run with mods yet, so as for mod installation, you'll have to look elsewhere for now.  I'll update once I start messing around with server mods.

##################
### EVENT LOOP ###
##################

Everything you need to get started is in the eventloops folder.  Map types are separated by different text files.  Each line in the text files is a different map and must keep that format, otherwise the script will break.

