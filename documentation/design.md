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
 - Encrypting / decrypting files before push / after pull 
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

Server side application
=======================
The server side as described initial documentation will run as a service on every node in the TuinWolk. The application would be dorment most of the time, waiting for user activity or node failure. A few components are key to the functioning of the TuinWolk service on a node: 

 - Git integration; 
 - Global system state checking; 
 - Distributed decision making. 

Git integration
---------------
 - git-shell ssh access throughout the system 
 - Git hooks to trigger the system on push
 
Global system state checking 
----------------------------
 - Periodic system knowledge update (using pings or custom network connection) 
 - Keep complete knowledge of repository locations 
 - Take action on node failure 
 - Use either fully connected graph of nodes or some smart (topology based?) x connections for each clients making sure all clients are equally connected 

Distributed decision making
---------------------------
 - No single node is more important than another 
 - Share and check information on system state 
 - Voting on possible decisions 
 - Detection of 'cheats' by malicious node(s) 

Distribution 
============
The TuinWolk applications--both the client and server sides--need to be distributable to multiple platforms or systems. The server side would most likely be targeted at unix-like systems due to the ssh dependency, but default locations and techniques for performing various actions differs from Debian to Gentoo or even BSD. Implementation differences between these platforms need to be taken into account. The client side application needs to run on as many platforms as possible for ease of use throughout the digital world. 
