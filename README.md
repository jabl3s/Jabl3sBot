# Jabl3sBot  
docker stylized assistant, with twitch and discord use etc etc  
![Alt text](assets/images/image.png)  

docker build -t jabl3s_bot:1.0 ./code  
docker tag jabl3s_bot:1.0 jabl3s/jabl3s_bot:latest  
docker push jabl3s/jabl3s_bot:latest  
docker run -it jabl3s/jabl3s_bot:latest  

---IN DEV RUN:::---  

docker-compose up -d --build  
docker-compose logs -f jabl3s_code_twitch  
docker-compose logs -f jabl3s_code_discord  
docker-compose down -v  

--- CLOSE ---  
Flush python output so that the compose logs can see wassup...
![Alt text](assets/images/image-1.png)  

  
