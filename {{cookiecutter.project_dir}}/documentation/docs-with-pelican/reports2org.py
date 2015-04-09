### * Description

# Simple script to convert generate an org file listing the html reports
# available
#
# The script gets the lists of folders and files in "./reports" and create an
# org file which will be processed into an html page as the other org files
# when the documentation is published

### ** Usage

# python script.py report_dir output_org_file

### * Setup

### ** Import

import sys
import os

### ** Parameters

REPORT_DIR = sys.argv[1]
RESOURCES_DIR = "resources"
OUTPUT_ORG_FILE = sys.argv[2]

### *** Prepare OUTPUT_HTML_FILE

if (OUTPUT_ORG_FILE.endswith(".org")) :
    OUTPUT_HTML_FILE = OUTPUT_ORG_FILE[:-3] + "html"
else :
    raise Exception("Output file does not have an org extension")

### ** Templates

ORG_HEADER = ("#+TITLE: HTML reports\n" +
              "#+URL: " + OUTPUT_HTML_FILE + "\n" +
              "#+Save_as: " + OUTPUT_HTML_FILE + "\n" +
              "#+Status: hidden\n" +
              "#+OPTIONS: toc:nil num:nil html-postamble:nil\n")

### * Functions

### ** getListSubDir(directory)

def getListSubDir(directory) :
    """Return the list of 
    """
    pass
    
### ** makeOrgBody(directory)

def makeOrgBody(directory) :
    """Make the body of the org file"""
    o = ""
    # Get the list of subfolders
    subfolders = [x for x in os.listdir(directory) if os.path.isdir(os.path.join(directory, x))]
    # For each subfolder
    for subfolder in subfolders :
        ## Create an org list itme
        o += "- " + subfolder + "\n"
        pel_dir = os.path.join(RESOURCES_DIR, REPORT_DIR, subfolder)
        ## Get the list of report files
        subPath = os.path.join(directory, subfolder)
        reportFiles = [x for x in os.listdir(subPath) if os.path.isfile(os.path.join(subPath, x))]
        ## For each report file
        for reportFile in reportFiles :
            link = os.path.join(pel_dir, reportFile)
            ### Insert a link entry
            o += "  - [[file:" + link + "][" + reportFile + "]]\n"
    # Return
    return(o)

### ** makeOrgHeader(header_template)

def makeOrgHeader(header_template):
    return (header_template + "\n")
    
### * Run

with open(OUTPUT_ORG_FILE, "w") as fo :
    fo.write(makeOrgHeader(""))
    fo.write(makeOrgBody(REPORT_DIR))

