FROM eclipse-temurin:21-jdk
WORKDIR /app
COPY eg2.java .
RUN javac eg2.java
CMD ["java","eg2"]