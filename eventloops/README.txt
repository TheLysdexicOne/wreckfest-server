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

First step would be to install python.
• https://www.python.org/downloads/windows/
• Windows x86-64 executable installer (if you have 64-bit windows)
• Windows x86 executable installer (if you have 32-bit windows)

Running the python script:

• Download the files from github and remember where you put them.
• Open cmd.exe on Windows
• cd <path-to-script>
• .\eventloop_creator.py

Alternatively,
• .\eventloop_creator.py > output.txt

This will output the results to a text file and overwrite it every time you run it.  ">>" will append it to the end of the output.txt file.  From there, copy the output and append it to the bottom "server_config.cfg" under the Event Loop section.

Start server and you should be good to go.

###########################################
### DEALING WITH BUGGY WRECKFEST SERVER ###
###########################################

Things to note about server:

• Sometimes when changing maps with special restrictions, the server doesn't actually change map.  Things to do:
	• Look at the server window and find the track that was supposed to load.  type "track <trackname>" and the map will change
	• Deal with it.  It's just more frustrating than an actual break in the server.
• Bots don't change chars when restrictions change
	• Once server loads with new configurations, just do the following codes in the server window...
		• bots 0
		• bots 24
	• This will get rid off all bots, then repopulate them with the correct restrictions.
	• If you change car_restriction through the server window, sometimes the bots will just get kicked and always have an invalid car. This usually applies when trying to set to restrict to a certain car in the pre-game lobby.
		• Use the following command in the server window: (this clear the car restrictions
			• car_restriction
			• car_class_restriction
		• From here, just use the in-game settings.  Under Server Options, set car restriction to "Host's Car".  This should fix the bots..should..should....this is one of the most buggy things about this.

Other than that, I haven't found too many issues.  Just having to reload the map occasionally and fix the bots.  If you plan to race with bots every race, I highly suggest refreshing them after every race for variety.  Just as soon as you're past the voiting screen, do the two "bots" commands.

Something to note, the command "/eventloop" will toggle the eventloop you have placed, so if you want to go back to manual configuration, just type "/eventloop" either in the lobby text box or in the server window.  This will give admin full control.


###############################
### LIST OF SERVER COMMANDS ###
###############################

Commands:
    list - print player list
    bans - print ban list
    admins - print list of user privileges
    clearusers - clear user privileges
    tracks - list tracks
    gamemodes - list game modes
    cars - list cars
    weathers - list weathers
    exit - close application
    ? - list server and event modifiers
Chat commands:
    /message [new message] - send a message to the chat
    /kick [id] - kick a player
    /ban [id] - ban a player
    /bansteamid [steam id] - ban a steam id
    /unban [ban index] - lift a ban, use "bans" for ban indices
    /unbansteamid [steam id] - lift a ban by steam id
    /clearbans - clear all bans
    /balanceteams - balance teams
    /restart - server restart
    /bot - add a bot
    /op [id] - add moderator privileges
    /opsteamid [steam id] - add moderator privileges by steam id
    /admin [id] - add admin privileges
    /adminsteamid [steam id] - add admin privileges by steam id
    /demote [id] - clear admin and moderator privileges
    /demotesteamid [steam id] - clear admin and moderator privileges by steam id
    /password [new password] - set password
    /servername [new server name] - set name of the server
    /welcome [new welcome message] - set the welcome message
    /eventloop - toggle automatic event rotation if configured











###NOTE: I'll probably update this a couple times, so keep an eye out for any changes.






























