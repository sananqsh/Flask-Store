FROM python:3.9

# Set working directory within container
WORKDIR /code

# Copy project files into container
COPY . /code

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port number on which Flask application will run
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
