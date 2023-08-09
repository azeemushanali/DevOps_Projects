# Notes
----------------------------------------------------
1-start initialising springboot app and test it in local - mvn spring-boot:run && mvn clean package to create a jar/war file.
2-set jenkins
3-set sonarqube
4-create sonarqube user token - squ_7ce257f73fd38da39bfb42a8ee0ab302d2d544ff
5-install sonarqube plugin,





----------------------------------------------------

For Maven Projects create a .java file in MVN-Project/src/main/java/test/sb/az/demo/

and run - mvn clean package - this is for cleaning old deployment and creating a new war file.

mvn spring-boot:run to re run the application



----------------------------------------------------


INstall argo CD 

1 - minikube start 
2 - kubectl configured
3 - curl -sL https://github.com/operator-framework/operator-lifecycle-manager/releases/download/v0.25.0/install.sh | bash -s v0.25.0  // from https://operatorhub.io/operator/argocd-operator
4 - kubectl create -f https://operatorhub.io/install/argocd-operator.yaml //run argocd operator

5 - go to operator Documenntaion -> Basics[https://argocd-operator.readthedocs.io/en/latest/usage/basics/] save it as yaml.
6 - Run kubectl apply -f argocd-controller.yml  //run argocd controller
7 - kubectl get pods to see if pods are running.
8 - Once pods are up and running use `kubectl get svc` 
9 - example-argocd-server This server is responbile for Argo CD UI
10 - `kubectl edit svc example-argocd-server` Use this and change `ClusterIP` to `NodePort`
11 - use `kubectl get svc` to check for the change
`
example-argocd-server           NodePort    10.105.39.79     <none>        80:30422/TCP,443:30576/TCP   7m15s
`
12 - Check for the pods are running and then run `minikube service example-argocd-server`. It will start the tunneling and start the we server.
`
example-argocd-server
|-----------|-----------------------|-------------|---------------------------|
| NAMESPACE |         NAME          | TARGET PORT |            URL            |
|-----------|-----------------------|-------------|---------------------------|
| default   | example-argocd-server | http/80     | http://192.168.49.2:30422 |
|           |                       | https/443   | http://192.168.49.2:30576 |
|-----------|-----------------------|-------------|---------------------------|
🏃  Starting tunnel for service example-argocd-server.
|-----------|-----------------------|-------------|------------------------|
| NAMESPACE |         NAME          | TARGET PORT |          URL           |
|-----------|-----------------------|-------------|------------------------|
| default   | example-argocd-server |             | http://127.0.0.1:54462 |
|           |                       |             | http://127.0.0.1:54463 |
|-----------|-----------------------|-------------|------------------------|
[default example-argocd-server  http://127.0.0.1:54462
http://127.0.0.1:54463]
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
`
13 - Use the ` http://127.0.0.1:54462` link given to open argo cd UI.
14 - Use username - admin and for password run - `kubectl get secret` and get `example-argocd-cluster` by running `kubectl edit example-argocd-cluster` because this is where the password is stored in `admin.password:` field.
15 - Since this is base64 encoded, to get the actual one use - `echo anJoSTZlZzBHeGF2WXFWa1h5bU4zOVV6Rm9UaWQ0Zmw= | base64 -d`. Copy without the last % symbol
16 - 
