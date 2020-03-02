nach talk-python course data-driven-web-app-with-flask ch15

Docker zum laufen bringen
========================= 
$ snap install docker


how-to-fix-docker-got-permission-denied-issue
=============================================
  
https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user  
https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue  

sudo groupadd docker  
sudo usermod -aG docker $USER  
Run the following command or Logout and login again and run (that doesn't work you may need to reboot your machine first)  
newgrp docker  
docker run hello-world  

  
