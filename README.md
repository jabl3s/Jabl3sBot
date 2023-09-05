# Jabl3sBot  
docker stylized assistant, with twitch and discord use etc etc  
![Alt text](assets/images/image.png)  
  
Consider installing harbor for self hosted repo benifits  
  
  
---PI specific:::---  Modify the eeprom config to have the following:::  
  
[all]
BOOT_UART=0
WAKE_ON_GPIO=1
POWER_OFF_ON_HALT=0
BOOT_ORDER=0xf14  

### (((SEE image five all this below doesnt fix usb boot, just goes into sd card reguardless)))

sudo rpi-eeprom-update -a  
sudo nano /etc/default/rpi-eeprom-config OR sudo rpi-eeprom-config --edit
BOOT_ORDER=0xf14  
  
1 is for USB boot.  
4 is for SD card boot.  
F signifies that if the preferred boot method (USB) fails, it should fall back to the secondary option (SD card).  
  
sudo rpi-eeprom-config --out /lib/firmware/raspberrypi/bootloader/critical/pieeprom.bin  
  
sudo shutdown -h now


---IN DEV RUN:::---  

docker-compose up -d --build  
docker-compose logs -f code_twitch_service  
docker-compose logs -f code_discord_service  
docker-compose down -v  

--- CLOSE ---  
Flush python output so that the compose logs can see wassup...  
![Alt text](assets/images/image-1.png)  
  
![Alt text](assets/images/image-2.png)
  
![Alt text](assets/images/image-4.png)  ![Alt text](assets/images/image-3.png)

################## CHATGPT  
In a microservices architecture where a service needs to both consume messages and perform other tasks concurrently, you can use multithreading or multiprocessing to achieve this. Here's a general approach using Python's `threading` module to run the message consumption and other tasks concurrently within the same service:

```python
import pika
import threading

# Define the RabbitMQ connection parameters
connection_params = pika.ConnectionParameters(
    host='localhost',  # Replace with your RabbitMQ server host
    port=5672,          # Default RabbitMQ port
)

# Create a connection to RabbitMQ
connection = pika.BlockingConnection(connection_params)

# Create a channel
channel = connection.channel()

# Specify the queue name you want to consume from
queue_name = 'your_queue_name_here'

# Define a callback function to process incoming messages
def callback(ch, method, properties, body):
    print(f"Received message: {body.decode('utf-8')}")

# Set up the consumer to use the callback function
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Function to start consuming messages
def consume_messages():
    print('Waiting for messages. To exit, press Ctrl+C')
    channel.start_consuming()

# Function for other tasks
def other_tasks():
    while True:
        # Perform other tasks here
        pass

# Create threads for message consumption and other tasks
consume_thread = threading.Thread(target=consume_messages)
other_tasks_thread = threading.Thread(target=other_tasks)

# Start both threads
consume_thread.start()
other_tasks_thread.start()

# Wait for both threads to finish (optional)
consume_thread.join()
other_tasks_thread.join()

# The code below will not execute until both threads are finished (optional)
print("All threads have finished.")
```

In this example:

1. We create two separate threads using Python's `threading` module: one for message consumption (`consume_messages()`) and another for other tasks (`other_tasks()`).

2. The `consume_messages()` function is responsible for consuming messages from the RabbitMQ queue using `channel.start_consuming()`. It runs in its thread.

3. The `other_tasks()` function represents any other tasks your microservice needs to perform concurrently. It runs in its thread as well.

4. Both threads are started concurrently using `consume_thread.start()` and `other_tasks_thread.start()`.

5. If you want to wait for both threads to finish before proceeding with the rest of the code, you can use `consume_thread.join()` and `other_tasks_thread.join()`. However, whether you use `join` or not depends on your specific requirements.

This approach allows your microservice to consume messages and perform other tasks simultaneously within the same service. You can adapt this structure to more complex scenarios or use multiprocessing if you need even more concurrency.