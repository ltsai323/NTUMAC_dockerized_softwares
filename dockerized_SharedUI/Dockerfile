# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    git \
    wget \
    curl \
    gnupg2 \
    lsb-release \
    apt-transport-https \
    software-properties-common \
    libgl1-mesa-glx \
    libx11-dev \
    x11-xserver-utils \
    && apt-get clean
RUn apt-get install -y libqt5gui5

# Install Python libraries
RUN pip install --no-cache-dir numpy PyQt5 jinja2 pytest pexpect requests

# Clone the Git repository
RUN git clone https://github.com/IncandelaLab/SharedUI.git

# Set the working directory
WORKDIR /SharedUI


# Set the entrypoint to run the Python script

ENTRYPOINT ["python3", "mainUI.py"]
