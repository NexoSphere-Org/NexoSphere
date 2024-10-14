# Use Ubuntu base image
FROM ubuntu:20.04

# Set your GitHub username and token as build arguments
ARG GITHUB_USERNAME
ARG GITHUB_TOKEN

# Set ENV variables that can be used in the container
ENV GITHUB_USERNAME=${GITHUB_USERNAME}
ENV GITHUB_TOKEN=${GITHUB_TOKEN}

# Update the package manager and install any packages you need
RUN echo "My variable is: ${GITHUB_USERNAME}" && \
    apt update && \
    apt install python3 -y && \
    apt install pip -y && \
    pip install flask && \
    apt-get install -y git && \
    cd /opt && \
    #clone the repo source code
    git clone -b nishant https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com/barualee/NexoSphere.git
    #unzip the source code
    # unzip main.zip

EXPOSE 5000
EXPOSE 443
