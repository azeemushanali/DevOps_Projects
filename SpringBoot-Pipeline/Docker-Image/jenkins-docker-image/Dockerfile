FROM jenkins/jenkins

USER root

# Install required packages to run Docker inside the Jenkins container
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release

# Add Docker repository key
RUN curl -fsSL https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]')/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker repository
RUN echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]') $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package lists again
RUN apt-get update

# Install Docker
RUN apt-get install -y docker-ce

RUN usermod -aG docker jenkins 


# Switch back to the Jenkins user
USER jenkins
