High level design
=================
Going from the initial ideas, the design of TuinWolk can be split into two parts: the client and the server. This document will describe the high level design of both in more detail, playing the part of a functional design. 

Client side application
=======================
As described in the initial documentation, the client side application will consist of three discrete parts, which are described in more detail below:

 - A service doing all the actual work; 
 - A file explorer integration component; 
 - A system integration widget (tray icon). 

Obviously, all three components need to work closely together to form a complete client side application. 

TuinWolk client service
-----------------------
 - Watch file system changes or periodically 'run' `git status` 
 - Keep open connection with TuinWolk to receive updates on available nodes, updates, ...
 - Split large changes in local repository into multiple commits 
 - Remove local unpushed commits to the same files to save space (only last edit of binary file would be backed up) 
 - Come up with commit messages more meaningful than time stamps and list of changed files 
 - Adhere to user settings (refresh if changed, see below) 

File browser integration 
------------------------
 - Indication of file being part of TuinWolk repo 
 - Show history of file 
 - Initiate user merge conflict resolvication 
 - Edit settings (see below) 

Tray icon
---------
 - Ability to pause activity (possibly abort commit) 
 - Indicator of status (changed files in (local|remote) repo / all up to date) 
 - Notify user of events (remote received push, pull from remote completed, push to remote completed, merge conflict) 
 - Edit settings (see below) 
 - Look into design details of DropBox

Available settings
------------------
 - Commit frequency (on write, daily, weekly, manual only, ...) 
 - Bandwith usage 
 - Preffered remote(s) to use 
 - Activity only on low system load 
 - Manage client side encryption passphrase 
 - Manage notification settings 
 - Move entire repository to new location 
