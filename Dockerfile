# Use an official, lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all your project files into the container
COPY . .

# Install your Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Make the startup script executable
RUN chmod +x run.sh

# Tell Hugging Face to listen to the Streamlit port
EXPOSE 7860

# Run the manager script when the container boots
CMD ["./run.sh"]