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
Implementation of the ideas found in this document has yet to take off, as is the implementation documentation and roadmap. 

Caveats
=======
Repository size and history
---------------------------
(large files will never leave the repo history, repo will only ever get bigger) 

Changes in the cloud
--------------------
(Although a temporary node failure will not hard the system, adding or removing nodes has to be done in a way that makes the change apparent to all other nodes and repos within the system) 

