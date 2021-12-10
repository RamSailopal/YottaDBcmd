# Introduction

![Alt text](yottacmd.webp?raw=true "Yottacmd")

A command line utility for YottaDB written in Python and utilising Typer

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
  
