FROM ubuntu:20.04

# Install Python and other dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    cron \
    && rm -rf /var/lib/apt/lists/*

RUN ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
RUN echo "America/Los_Angeles" > /etc/timezone

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

RUN python3 src/main.py

# Add crontab file
COPY crontab /etc/cron.d/crontab

# Give execution rights on the cron job
RUN chmod 0744 /etc/cron.d/crontab

# Apply cron job
RUN crontab /etc/cron.d/crontab

RUN touch /var/log/cron.log

# Start cron daemon and run the Python script
CMD cron && tail -f /var/log/cron.log
