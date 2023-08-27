# Use the official Python image as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

COPY . .
# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot script when the container starts
CMD ["python", "-u", "Bot.py"]