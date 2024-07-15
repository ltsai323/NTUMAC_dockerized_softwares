# Build docker image with X11 service
## installation
* Windows 10 22H2
* Docker Desktop
* VcXsrv

### Notes

Use `host.docker.internal:0` handling X11 name server.
```
docker run --env="DISPLAY=host.docker.internal:0" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" check-x11
```


