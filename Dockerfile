FROM python:3.8-slim-buster

# Set work directory
WORKDIR /app

# Update system and install dependencies including curl
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    python3-dev \
    default-libmysqlclient-dev \
    gcc \
    gnupg \
    g++ \
    unixodbc-dev

# Install Microsoft ODBC 17 Driver for SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Copy requirements file and install Python dependencies
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

# Set the environment file
ARG ENV
COPY ${ENV} /app/

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
