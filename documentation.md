History
=======
TuinWolk is an idea instigated by Peter 'Sakartu' Wagenaar and Mattijs 'akaIDIOT' Ugen after starting to use git to backup files they didn't want to lose in the case of local computer apocalypse. Rather than just copying files to another site, versioning everything with git allows for retrieval of old versions of files in case something was overwritten or eaten by hardware. 

As git is a distributed system by design, the backup solution described here could be made distributed as well. Enter a few beers and a sudden eureka moment and the general idea behind TuinWolk was born. The name is derived from the combination of TuinfeesT--the name of a group of friends from Enschede, The Netherlands--and wolk, the Dutch word for cloud. 

General idea
============
The general idea behind TuinWolk is to create a distributed backup solution powered by the git version control system. Although git might not be the default choice to backup all kinds of files, many of the inteded users are already familiar with it and are hence convinced of its power. 

Users of TuinWolk turn a folder on their system into a git repository to start use of the backup system. Local changes to files in this directory will be tracked by git and users can commit these changes as they see fit. After committing changes, they can push these changes to a server that is part of the cloud of systems running TuinWolk. Each of these systems will contain a copy of the user's repository, so pushing changes to this repository will update that system's copy to be up to date with the state of the documents on the user's personal system. As TuinWolk is inteded to work as a cloud, the server that received an update of the user's repository now has the responsibility to synchronize the repository with other nodes in the cloud. When all nodes are up to date, a user can clone the repository from any of the nodes to create a local copy of his or her backed up files. 

Implementation
==============
Implementation of the ideas found in this document has yet to take off, as is the implementation documentation and roadmap. See the 'Components' section for currently planned components of the system. 

As many of the people in TuinfeesT have a relatively idle personal server in various locations, deployment of the cloud will be done across these personal servers. As the servers have different owners who all have root privileges on their own machine, use of TuinWolk involves trusting the owners of the involved machines with your files. Likewise, owners of TuinWolk nodes are expected to respect the privacy of all TuinWolk users and keep their paws off other people's files. 

Administrators are classicly lazy, as is TuinfeesT. The system needs to be setup in a way that minimizes user interaction other than using it as a backup solution. 

Components
==========
In order to make TuinWolk more useful to its users, a number of components are to be developed on top of the git version control system. 

Server-side synchronization
---------------------------
In order to make TuinWolk act as a cloud service, each node in the cloud will have to automatically synchronize pushed changes to other nodes in the cloud. 

It is logical to use git hooks for this. When pushing between nodes, however, care needs to be taken that nodes will not keep pushing empty changesets in circles; updates need to be sent around somewhat intelligently. With an initial low amount of nodes, this could be accomplishes by having the receiver of a user's push be the one to update all other nodes. Should the system ever scale up, this is no longer feasible. If an elegant solution is not found initially, implementation of such a distribution algorithm could be postponed to a more troublesome time. 

Nodes in the system need to be aware of each other's presence in order to know where to push to. Use of a single master node that maintains this information is considered a bad idea; all nodes sharing knowledge of the complete network is more robust. Entering a new node into the system would then require a system administrator to point the new node to at least one other node in order to retrieve information on the other nodes, however. Use of some sort of round robin or dynamic DNS pointing to a preset hostname might ease the pain in most cases. 

Administration tools
--------------------
Administrators need to be able to add a repository for a new user without too much hassle. Scripts that require only a user and create a new repository that will be assimilated into the cloud would obviously increase the amount of administrator lazy. 

A manual forced synchronization attempt could be useful in case of system malfunction or a node having been offline and needing to update all repositories. 

Desktop integration
-------------------
For every operating system in use by TuinWolk's users (currently Linux, Max OSX and Windows), the following components will ease the use of the system and turn it into a proper backup solution: 

 - (Headless) client component with knowledge of local TuinWolk repositories and cloud nodes (probably just git remotes) and capabilities to refresh any knowledge about the cloud from any TuinWolk node. The component should automatically pull changes not present in the local repository from the cloud (at startup, periodically, by push notification, ...). 
 - File explorer (Nautilus/Thunar/Finder/Explorer) extension that communicates with the client component to manage local TuinWolk repositories. 
 - System widget capable of indicating changes ready to commit or push and communicating with the client component. 

For Linux and Mac OSX, python might be used as this allows to integrate into the system well. For Windows, someone might be sharpening some C. 

Setup
=====
TODO: expand writing (insert epic fail here T_T)
 - acolyte sends ssh pubkey to estrablished admin 
 - admin pushes new autorized keys file through cloud 
 - acolyte's server has git access to entire cloud
 - new node pulls appropriate repos to local file system 

Communication
=============
TODO: expand writing (also insert fila here...)
 - nodes need to communicate other things than just git 
 - setup encrypted sockets with known secrets or secrets pushed in a git config (git access was established first anyway) 

Roadmap
=======
TuinfeesT is not known for its planning skills. Therefore, this section does not have a lot of meaningful content (yet). 

Future extensions
=================
 - Custom replication level (don't store every user's repository on every node, making the system a lot more scalable). 
 - Web interface (so only a login is needed for downloading a single file in stead of cloning a full repository). 
 - Resetting of a user's repository (removing all history information and old, large, unneeded files). 

Caveats
=======
Repository size and history
---------------------------
(large files will never leave the repo history, repo will only ever get bigger) 

Changes in the cloud
--------------------
(Although a temporary node failure will not hurt the system, adding or removing nodes has to be done in a way that makes the change apparent to all other nodes and repos within the system) 

