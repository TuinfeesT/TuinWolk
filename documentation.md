History
=======
TuinWolk is an idea instigated by Peter 'Sakartu' Wagenaar and Mattijs 'akaIDIOT' Ugen after starting to use git to backup files we didn't want to lose in the case of local computer apocalypse. Rather than just copying files to another site, versioning everything with git allows for retrieval of old versions of files in case something was overwritten or eaten by hardware. 

As git is a distributed system by design, the backup solution described here could be made distributed as well. Enter a few beers and a sudden eureka moment and the general idea behind TuinWolk was born. The name is derived from the combination of TuinfeesT --the name of a group of friends from Enschede, The Netherlands-- and wolk, the Dutch word for cloud. 

General idea
============
The general idea behind TuinWolk is to create a distributed backup solution powered by the git version control system. Although git might not be the default choice to backup all kinds of files, many of the inteded users are already familiar with it and are hence convinced of its power. 

Users of TuinWolk turn a folder on their system into a git repository to start use of the backup system. Local changes to files in this directory will be tracked by git and users can commit these changes as they see fit. After committing changes, they can push these changes to a server that is part of the cloud of systems running TuinWolk. Some or each of these systems will contain a copy of the user's repository, so pushing changes to one repository will update that system's copy to be up to date with the state of the documents on the user's personal system. As TuinWolk is inteded to work as a distributed system, the server that received an update of the user's repository now has the responsibility to synchronize the repository with other nodes in the cloud. When all nodes are up to date, a user can clone the repository from any of the nodes to create a local copy of his or her backed up files. 

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

It is logical to use git hooks for this. When pushing between nodes, however, care needs to be taken that nodes will not keep pushing empty changesets in circles; updates need to be sent around somewhat intelligently. With an initial low amount of nodes, this could be accomplishes by having the receiver of a user's push be the one to update all other nodes. Should the system ever scale up, this is no longer feasible. If an elegant solution is not found initially, implementation of such a distribution algorithm could be postponed to a more troublesome time. One could, for instance, think of a spanning tree protocol in which each node is responsible for the pushes to a certain server. This, in combination with a heartbeat service and a redesign-tree-when-node-collapses protocol should be enough to guarantee uptime.

Nodes in the system need to be aware of each other's presence in order to know where to push to. Use of a single master node that maintains this information is considered a bad idea; all nodes sharing knowledge of the complete network is more robust. Entering a new node into the system would then require a system administrator to point the new node to at least one other node in order to retrieve information on the other nodes, however. Use of some sort of round robin or dynamic DNS pointing to a preset hostname might ease the pain in most cases. 

In the case of large changes to the system--like pushing a large user commit between nodes or synchronizing a repository copy to a new node--bandwidth usage from node to node needs to be kept in check to not clog the network between the nodes. How to tell git to throttle the network throughput is something to research. 

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

For Linux and Mac OSX, python might be used as this integrates into the system well. For Windows, someone might be sharpening some C. 

As home connections to the Internet are not always as fast as a user would want, the client program will have to take bandwidth limitations into account. With large changes to a user's repository, the client program will have to split the change into commits of a particular size and push them into the cloud one by one, possibly periodically. 

New Node Setup
==============
If a person (from now on referred to as an acolyte) wants to join an existing TuinWolk with server A, he/she will have to make contact with an existing TuinWolk administrator. The acolyte provides his/her public key to the administrator, who adds this key to his/her own server (B). The file in which all these keys are stored is part of the TuinWolk and is thus pushed to all other servers, giving the acolyte git access on all servers in the cloud and giving all other servers in the cloud access to the acolyte's server in return. The acolyte can now setup and start running the TuinWolk daemon which will (together with the other daemons) decide which repositories the acolyte's server will host, depending on the amount of storage the acolyte donates to the TuinWolk.

Communication
=============
In order for the daemons to decide which repositories will be stored where (see New Node Setup above and Caveats below), the daemons will have to communicate on a live channel instead of just through files in git. To encrypt these communcations, however, we can setup a simple public/private key encryption system in which the public keys of nodes are distributed through git. In this way we can use a simple socket as a communication means between servers over which we send encrypted commands and such. This communication is secure against eavesdroppers but might not stop active man-in-the-middle attackers. Hashing and signing each message, however, should resolve this issue.

Roadmap
=======
TuinfeesT is not known for its planning skills. Therefore, this section does not have a lot of meaningful content (yet). 

Future extensions
=================
 - using information from http://syncom.appspot.com/papers/git_encryption.txt, try to make the cloud storage encrypted.
 - Custom replication level (don't store every user's repository on every node, making the system a lot more scalable). 
 - Web interface (so only a login is needed for downloading a single file in stead of cloning a full repository). 
 - Resetting of a user's repository (removing all history information and old, large, unneeded files). 

Caveats
=======
Repository size and history
---------------------------
As each user can decide for him/herself how much space to donate to the TuinWolk, repository size might become a problem. Two mitigations exist to solve this problem:

1. Git provides the git-rebase functionality, making it possible to 'forget' all revisions before a certain chosen revision. Using this system, one could decide that revisions which are over 2 years old are probably no longer of use and can thus be removed from the repository. The largest repositories, however, will probably contain large binary files (such as pictures) which hardly have any revisions, making this mitigation a bit less useful.
2. Let the daemons decide for themselves which repository is stored where. If a repo is comprised of mainly large binary files the system could decide that it is probably a photo backup (and not a source directory) and can thus only replicate this repo on systems that have plenty of storage available to the TuinWolk. Although this creates some unfairness (people adding only 10GB to the total TuinWolk size can still place repositories > 10GB) it does provide a solid solution to the problem. Furthermore, the unfairness is eased a bit since adding large repo's to the TuinWolk means that they will be stored only in a few places (namely only machines with lots of storage) and will thus not be available on every machine in the TuinWolk.

Changes in the cloud
--------------------
Failure of TuinWolk systems should never result in dataloss; that is TuinWolk's main feature. This means that temporary or pertinent downtime of a system should be detected and handled gracefully. A distributed heartbeat system can be used to detect system failure, this should be easy to setup.  If the dying system is one of two systems hosting a certain repo (it can never be the only one), the TuinWolk should then replicate the repo to another system, to make sure that there are always at least two copies.

