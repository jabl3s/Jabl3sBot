# jabl3s_bot  
---IN DEV RUN:::---  

docker-compose up -d --build  
docker-compose logs -f service_discord    
docker-compose logs -f service_twitch  
docker-compose logs -f service_rabbitmq   
docker-compose down -v  
  
--- CLOSE ---  
Flush python output so that the compose logs can see wassup...  
![Alt text](assets/images/image-1.png)  
  
![Alt text](assets/images/image-2.png)
  
![Alt text](assets/images/image-4.png)  ![Alt text](assets/images/image-3.png)
