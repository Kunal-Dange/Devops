FROM openjdk:8
EXPOSE 8080
ADD Devops/springboot-k8s-demo.jar springboot-k8s-demo.jar
ENTRYPOINT ["java","-jar","/springboot-k8s-demo.jar"]
