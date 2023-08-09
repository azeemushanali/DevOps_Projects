# Use the official Docker-in-Docker (DinD) image as the base image
FROM docker:dind

# Install required packages to run Maven
RUN apk update && apk add --no-cache curl tar

# Set the environment variables for Maven
ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_VERSION 3.8.4

# Install Maven
RUN mkdir -p /usr/share \
    && curl -fsSL https://mirror.navercorp.com/apache/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz | tar -xzf - -C /usr/share \
    && ln -s /usr/share/apache-maven-${MAVEN_VERSION} /usr/share/maven \
    && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

# Set the Maven path in the environment
ENV PATH /usr/share/maven/bin:$PATH
