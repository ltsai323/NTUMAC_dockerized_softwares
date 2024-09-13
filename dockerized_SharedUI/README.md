# SharedUI
SharedUI is written in bash, Power Shell in windows is not able to execute this program. So we used docker to execute this code.
Original code is [here](https://github.com/IncandelaLab/SharedUI).

# how do use it
1. Install docker desktop application from offical webpage.
1. Install VcXsrv application from offical webpage.
1. (Optional) Overwrite **filemanager_data** from [other source](https://drive.google.com/drive/folders/1Geyf9KwpQOncLSZAvq2nZIrNbzvG-S12?usp=drive_link).
1. Double click "init.bat"
1. Double click "run.bat"

# Descriptions of the batch file
## init.bat
The purpose of this file builds a customized docker image from DockerFile.
1. Check docker desktop is running or not.
1. If old docker image exists, delete it.
1. Run "docker build" command.

## DockerFile
Prepare a Python3.10-slim environment and download latest version of SharedUI from github.


## run.bat
Execute command "docker run" with options.
Also check the software dependencies activated before run the docker command.
1. Check docker desktop is running or not.
1. Check VcXsrv is running or not. If not, open VcXsrv using `../config.xlaunch` configuration.
1. docker run with options
    - X11 setup
    - Synchronize **filemanager_data** at current directory.
    - Access `${HOME}/.ssh` for ssh login requirement.


# Note
The result would be recorded into **filmanager_data** with json format. You can back up or access for other purpose. All input values are recorded into **filemanager_data** simultaneously.


