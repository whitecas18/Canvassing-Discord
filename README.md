# Canvassing-Discord
Canvassing-Discord  

To run Canvas-Bot, open a command line in the main project folder and type: pyhton bot.py  
If succesful, you will get the message 'Canvas-Bot#2788 has connected to Discord!'  

Once Canvas-Bot is connected, you need to add it to the server you plan to use it on.  

https://discord.com/oauth2/authorize?client_id=751477398029074514&scope=bot&permissions=0  
To use invite the bot to a server copy this paste the above link into your browser.  
From here you can choose which server you want to bot to be added to.  
(NOTE: You must have the "Manage Permission's" Permission on the server you wish to add the  
bot to.  


#######################################################  
Changing What Course Canvas-Bot Pulls Annoucements From  
#######################################################  

The course Canvas-Bot pulls its information from is determined by the institution code and the class code.  
These values are assigned to the instCode and classCode variables respectively. Both of these variables   
can be pulled the URL of a standard Canvas Course page. For example,  
https://ecu.instructure.com/courses/12345  
         ^                           ^  
  instCode(school intials)   classCode(digits after the /)  


In the current implementation, the instCode and classCode have to be hardcoded for the bot to run properly,  
but we are currently working on bot commands to allow these values to be updated.  
