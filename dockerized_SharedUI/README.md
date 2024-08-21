# SharedUI
SharedUI is written in bash, Power Shell in windows is not able to execute this program. So we used docker to execute this code.
Original code is [here](https://github.com/IncandelaLab/SharedUI).

# how do use it
* Open Docker Desktop
* Load VcXsrv configurations
* (Optional) Overwrite **filemanager_data** from [other source](https://drive.google.com/drive/folders/1Geyf9KwpQOncLSZAvq2nZIrNbzvG-S12?usp=drive_link).
* Double click **ssh_login_for_first.bat** for initializing DBLoader connection via SSH (Every lxplus account requires executing this script.)
* Double click **init.bat** for building docker image from docker file. (Once you built the docker image, you can skip this step.)
* Double click **run.bat** for activating docker container from built docker image.


# Note
The result would be recorded into **filmanager_data** with json format. You can back up or access for other purpose. All input values are recorded into **filemanager_data** simultaneously.


