docker rm  check-x11-container
docker rmi check-x11-image

docker build -t check-x11-image .
docker run --env="DISPLAY=host.docker.internal:0" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --name check-x11-container check-x11-image

echo FINISHED
pause
