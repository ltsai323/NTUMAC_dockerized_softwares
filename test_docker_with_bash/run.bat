docker rm  check-ssh-container
docker rmi check-ssh-image

docker build -t check-ssh-image .
docker run -d ^
           -p 2222:22 ^
           --volume "%USERPROFILE%\.ssh:/root/.ssh:rw" ^
	       --name check-ssh-container check-ssh-image

echo FINISHED
pause
