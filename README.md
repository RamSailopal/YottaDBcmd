# Introduction

![Alt text](yottacmd.webp?raw=true "Yottacmd")

A command line utility with command line completion for YottaDB written in Python and utilising Typer

Commands:

  **command**       - Execute a YottaDB command
  
  **configview**     - View YottaDB environmental variables
  
  **databasesize**   - Database size statistics.
  
  **globaledit**     - Edit a global in YottaDB
  
  **globallist**     - Display a list of globals in YottaDB
  
  **globalsearch**   - Search global(s) for a specific string.
  
  **globalview**    - View a global/global subscript in YottaDB
  
  **prompt**         - Enter YottaDB to execute commands
  
  **routineedit**    - Edit and compile a routine from YottaDB
  
  **routinelist**    - Display a list of routines in YottaDB
  
  **routinesearch**  - Search routine(s) for given string.
  
  **routineview**    - Display a routine from YottaDB
  
  **version**        - Display the version of YottaDB
  
# Requirements

A working version of YottaDB is required on the same machine as where this utility is installed. You should also be able to execute YottaDB commands from anywhere i.e. with ydb.

This can be acheived with:

    ln -s /usr/local/bin/ydb <path to yottadb executable>
  
# Installation

    git clone https://github.com/RamSailopal/YottaDBcmd.git
    cd YottaDBcmd
    ./install.sh
  
 Restart your terminal to allow command completion to take effect
 
 Run commands i.e **yottacmd globallist**
 
 # Executing commands remotely
 
 Encrypted commands can be run remotely against the YottaDB server by running the yottacmd-server process. To set up and run on the YottaDB server:
 
 1) Change the username and password as well as port if required in the yottacmd ini file.
 2) Run **python3 -m pip install pycrypto**
 3) Run **./yottaserver.sh start** to start the server process (the process can then be checked with **./yottaserver.sh status** or stopped with .**/yottaserver.sh stop**)

On the remote client, clone the repo or attain the **yottacmd-remote** executable and then run the command against the server i.e.

    python3 -m pip install pycrypto
    ./yottacmd-remote -U Yotta -P "Access-Please" -p 4001 -s "192.168.1.5" -c 'globallist'
    
 **Pre-requisites**
 
 Pycrypto requires that the **python3-devel** package is installed and so install this before running pip install pycrypto
 

 # Docker
 
 https://hub.docker.com/r/ramb0/yottadbcmd
 
 # Docker Compose
 
 https://github.com/RamSailopal/YottaDBcmd/tree/main/compose

