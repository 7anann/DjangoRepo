# 1. Start with a Python "Base Image"
FROM python:3.12-slim

# 2. Set environment variables to keep Python from acting weird in a container
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Create a folder for your app inside the container
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your project files into the container
COPY . /app/

# 6. Tell the container to start Waitress when it launches
CMD ["waitress-serve", "--port=8000", "myproject.wsgi:application"]

