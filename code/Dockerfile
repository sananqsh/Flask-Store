FROM python:3.5

# Set working directory within container
WORKDIR /code

# Copy project files into container
COPY . /code

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Patch incompatible files
RUN apt-get install -y patch
RUN patch /usr/local/lib/python3.5/site-packages/jwt/api_jwt.py < patches/api_jwt.patch
RUN patch /usr/local/lib/python3.5/site-packages/jwt/api_jws.py < patches/api_jws.patch

# Expose the port number on which Flask application will run
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
