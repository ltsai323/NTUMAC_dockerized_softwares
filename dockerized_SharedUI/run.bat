docker run -it --rm ^
  --env="DISPLAY=host.docker.internal:0" ^
  --env="QT_X11_NO_MITSHM=1" ^
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" ^
  --volume="%cd%\filemanager_data:/SharedUI/filemanager_data" ^
  --name shared-ui-container shared-ui-image

echo FINISHED
pause
