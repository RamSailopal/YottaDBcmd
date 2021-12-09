#!/usr/bin/python3
import typer
import subprocess
import re
import fnmatch
import os

app = typer.Typer()

@app.command()
def version():
    cmd = "ydb <<< 'W $ZV' | awk '!/^$/&&!/>$/ { print }'"
    process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
    result = process.communicate()
    result1=result[0].decode('utf-8')
    print("\nYottaDB Version\n")
    print(result1)


@app.command()
def globallist(glbal: str="*"):
    cmd = "ydb <<< 'D ^%GD;*' | awk '/^Global/ { prnt=1;next } /^Total of/ { prnt=0 }prnt'"
    process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
    result = process.communicate()
    result1=result[0].decode('utf-8').replace(" ","")
    result1=result1.replace("\n","")
    result1=result1.replace("^","\n^")
    print("\nGlobals in YottaDB\n")
    result2=result1.split("\n")
    for glob in result2:
       if ( fnmatch.fnmatch(glob,glbal) ):
          print(glob)

@app.command()
def routinelist(routine: str="*"):
    cmd = "(echo D ^%RD;sleep 1;echo \"*\";sleep 1;echo \"\";echo \"H\") | ydb | awk '/^Routine/{ prnt=1;next } /^Total of/||/>$/ { prnt=0 }prnt'"
    process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
    result = process.communicate()
    result1=result[0].decode('utf-8').replace(" ","\n")
    result1 = re.sub(r'\n+', '\n', result1).strip()
    print("\nRoutines in YottaDB\n")
    result2=result1.split("\n")
    for rout in result2:
       if ( fnmatch.fnmatch(rout,routine) ):
          print(rout)

	

@app.command()
def globalview(glbal: str):
    cmd = "(echo \"D ^%G\";echo \"\";echo \"" + glbal + "\";echo \"\")|ydb | awk '/^List/ { prnt=1;next } /^$/ { prnt=0 }prnt'"
    process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
    result = process.communicate()
    result1=result[0].decode('utf-8').replace(" ","\n")
    result1 = re.sub(r'\n+', '\n', result1).strip()
    print("\nYottaDB Global view for ^" + glbal + "\n")
    print(result1)

@app.command()
def globalsearch(glbal: str, searchstr: str):
    cmd = "(echo \"D ^%GSE\";echo \"\";echo \"" + glbal + "\";echo \"\";echo \"" + searchstr + "\")|ydb | awk '/^Find string:/ { prnt=1;next } /^Total/ { prnt=0;next }prnt'"
    process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
    result = process.communicate()
    result1=result[0].decode('utf-8')
    print("\nSearching global " + glbal + " for search string " + searchstr + "\n")
    print(result1)


@app.command()
def globaledit(ref: str):
    cmd = "ydb <<< 'W $G(" + ref + ")' | awk '!/^$/&&!/>$/ { print }'"
    process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
    result = process.communicate()
    result1=result[0].decode('utf-8').replace(" ","\n")
    print("\nYottaDB Global edit for " + ref + "\n")
    print(result1)
    resp=input("Do you wish to amend? (Y/N) ")
    if ( resp =="Y" ):
       resp1=input("Enter new value ")
       resp2=input("Set " + ref + " to " + resp1 + "? (Y/N) ")
       if ( resp2 == "Y" ):
          os.system("ydb <<< 'S " + ref + "=\"" + resp1 + "\"'")  
          cmd = "ydb <<< 'W $G(" + ref + ")' | awk '!/^$/&&!/>$/ { print }'"
          process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
          result = process.communicate()
          result1=result[0].decode('utf-8').replace(" ","\n")
          print("New value:\n" + ref + "=" + result1 + "\n")




@app.command()
def routineview(routine: str):
    cmd = "ydb <<< \"W \$ZRO\" | awk '!/^$/&&!/>$/ { print }'"
    process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
    result = process.communicate()
    result1=result[0].decode('utf-8')
    print("\nYottaDB Routine view for ^" + routine + "\n")
    result1=result1.replace("("," ")
    result1=result1.replace(")"," ")
    result1=result1.replace("*"," ")
    result1 = re.sub(r'\n+', '\n', result1).strip()
    result2=result1.split(" ")
    for path in result2:
        if ( path != "" and not fnmatch.fnmatch(path,'*.so') ):
          cmd="find " + path + " -name \"" + routine + ".m\" -exec cat '{}' \\;"
          process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
          result = process.communicate()
          result1=result[0].decode('utf-8')
          if (result1 != ""):
             print(path + "/" + routine + ".m\n\n\n\n" + result1)



@app.command()
def routineedit(routine: str, nocompile: bool = False):
    cmd = "ydb <<< \"W \$ZRO\" | awk '!/^$/&&!/>$/ { print }'"
    process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
    result = process.communicate()
    result1=result[0].decode('utf-8')
    result1=result1.replace("("," ")
    result1=result1.replace(")"," ")
    result1=result1.replace("*"," ")
    result1 = re.sub(r'\n+', '\n', result1).strip()
    result2=result1.split(" ")
    for path in result2:
        if ( path != "" and not fnmatch.fnmatch(path,'*.so') ):
          cmd="find " + path + " -name \"" + routine + ".m\""
          process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
          result = process.communicate()
          result1=result[0].decode('utf-8')
          if (result1 != ""):
             print("\nEditing routine -  ^" + routine + "\n")
             os.system('vi ' + result1 + ' </dev/tty >/dev/tty 2>&1')
             if ( not nocompile ):
               print("\n\nCompiling routine - " + routine + "\n\n")
               os.system("ydb <<< 'ZL \"" + routine + ".m\"'")

@app.command()
def configview():
    cmd = "bash -c \"source /usr/local/yottadb/ydb_env_set && env | grep -E '(ydb|gtm)'\""
    process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
    result = process.communicate()
    result1=result[0].decode('utf-8')
    print("\nYottaDB Configuration environmental variables\n")
    print(result1)

@app.command()
def prompt():
    os.system("ydb")


if __name__ == "__main__":
    app()
