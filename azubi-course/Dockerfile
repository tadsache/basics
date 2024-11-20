# Use the official Ubuntu image as the base
FROM ubuntu:latest

# Update package lists and install SSH, Ansible, and Python
RUN apt-get update && \
    apt-get install -y openssh-server ansible python3-pip && \
    apt-get clean

# Set up SSH
RUN mkdir /var/run/sshd && \
    echo 'root:password' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config

# Generate SSH keys for the root user
RUN ssh-keygen -A

# Set environment variable to avoid Ansible warnings
ENV ANSIBLE_HOST_KEY_CHECKING=False

# Expose SSH port
EXPOSE 22

# Start SSH service when the container starts
CMD ["/usr/sbin/sshd", "-D"]

