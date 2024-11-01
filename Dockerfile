# Use Ubuntu base image
FROM ubuntu:20.04

# Set your GitHub username and token as build arguments
# ARG GITHUB_USERNAME
# ARG GITHUB_TOKEN

# Set ENV variables that can be used in the container
# ENV GITHUB_USERNAME=${GITHUB_USERNAME}
# ENV GITHUB_TOKEN=${GITHUB_TOKEN}

# Update the package manager and install any packages you need
RUN apt update && \
    apt install python3 -y && \
    apt-get install -y git && \
    cd /opt && \
    #clone the repo source code
    # git clone -b nishant https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com/barualee/NexoSphere.git && \
    #run installs
    apt install pip -y

WORKDIR /app
COPY ./sourceCode .
# Copy requirements.txt first (this helps with caching layers)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9874
EXPOSE 443
