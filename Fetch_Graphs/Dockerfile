FROM robcherry/docker-chromedriver:latest

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev python3-pip cron

RUN mkdir -p /app
WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./Fetch_Graphs /app
COPY ./DataDriver /app/DataDriver

# Copy hello-cron file to the cron.d directory
# COPY ./Fetch_Graphs/fetch_cron /etc/cron.d/fetch_cron

# Give execution rights on the cron job
# RUN chmod 0644 /etc/cron.d/fetch_cron

# Apply cron job
# RUN crontab /etc/cron.d/fetch_cron

# Create the log file to be able to run tail
# RUN touch /var/log/cron.log

RUN pip3 install -r requirements.txt
RUN chmod +x run.sh

ENTRYPOINT [ "bash" ]

# CMD [ "python3", "Fetch.py" ]
# CMD [ "python3", "Graphs.py" ]
CMD ["./run.sh"]
# Run the command on container startup
# CMD cron && tail -f /var/log/cron.log
