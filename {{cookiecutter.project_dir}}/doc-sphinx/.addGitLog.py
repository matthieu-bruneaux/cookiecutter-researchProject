### * Setup

### ** Import

import subprocess
import argparse
import ansi2html
import sys

### ** Parameters

INSERT_GIT_STRING = "lastGitLog"

### ** Parser

parser = argparse.ArgumentParser()
parser.add_argument("inputFile", metavar = "INPUT", type = str,
                    nargs = 1)
parser.add_argument("outputFile", metavar = "OUTPUT", type = str,
                    nargs = 1)

### * Functions

### ** getGitLog(nLines)

def getGitLog(nLines) :
    if nLines == "all" :
        command = ["git", "log", "--graph", "--abbrev-commit",
                   "--decorate", "--date=local", "--all",
                   "--format=format:%C(bold green)(%ad)%C(reset) %C(white)%s%C(reset) %C(bold blue)(%h)%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)"]
    else :
        command = ["git", "log", "-" + str(nLines), "--graph", "--abbrev-commit",
                   "--decorate", "--date=local", "--all",
                   "--format=format:%C(bold green)(%ad)%C(reset) %C(white)%s%C(reset) %C(bold blue)(%h)%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)"]
    gitLogP = subprocess.Popen(command,
                               stdout = subprocess.PIPE)
    (gitLogAnsi, gitLogErr) = gitLogP.communicate()
    converter = ansi2html.Ansi2HTMLConverter()
    gitLogHtml = converter.convert(gitLogAnsi, full = False)
    preamble = "<pre class=\"ansi2html-content\">\n"
    postamble = "</pre>\n"
    return preamble + gitLogHtml + postamble

### ** getGitLogAll()

def getGitLogAll() :
    command = ["git", "log", "-" + str(nLines), "--graph", "--abbrev-commit",
               "--decorate", "--date=local", "--all",
               "--format=format:%C(bold blue)%h%C(reset) %C(bold green)(%ad)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)"]
    gitLogP = subprocess.Popen(command,
                               stdout = subprocess.PIPE)
    (gitLogAnsi, gitLogErr) = gitLogP.communicate()
    converter = ansi2html.Ansi2HTMLConverter()
    gitLogHtml = converter.convert(gitLogAnsi, full = False)
    preamble = "<pre class=\"ansi2html-content\">\n"
    postamble = "</pre>\n"
    return preamble + gitLogHtml + postamble
    
### * Run

### ** Insert git output

args = parser.parse_args()
output = ""
with open(args.inputFile[0], "r") as fi :
    for line in fi :
        if "&lt;" + INSERT_GIT_STRING + "-" in line :
            start = line.split("&lt;" + INSERT_GIT_STRING + "-")[0]
            end = line.split("&lt;" + INSERT_GIT_STRING + "-")[1].split("&gt;")[1]
            n = line.split("&lt;" + INSERT_GIT_STRING + "-")[1].split("&gt;")[0]
            line = start + getGitLog(n) + end
        output += line
with open(args.outputFile[0], "w") as fo :
    fo.write(output)

