# ☸️ Kubernetes Test Application

A simple Flask web application built to learn and practice **Docker, Kubernetes, and Minikube**.

The application provides a small form where users can enter their **name and email**. The Flask application is containerized using Docker and deployed to a local Kubernetes cluster using **Minikube**.

---

## 🚀 Project Overview

This project was created while learning the fundamentals of Kubernetes.

The application demonstrates how to:

- Build a Flask web application
- Containerize the application using Docker
- Create a Docker image
- Deploy the container using Kubernetes
- Run multiple replicas using a Kubernetes Deployment
- Expose the application using a Kubernetes Service
- Run Kubernetes locally using Minikube
- Understand Pods, Deployments, Services, and containers
- Access a Kubernetes application from a local machine

---

## 🏗️ Architecture

```text
                 ┌──────────────────────┐
                 │      User/Browser     │
                 └──────────┬───────────┘
                            │
                            │ Port 8080
                            ▼
                 ┌──────────────────────┐
                 │ Kubernetes Service   │
                 │   Port: 8080         │
                 └──────────┬───────────┘
                            │
                     targetPort: 5000
                            │
             ┌──────────────┴──────────────┐
             │                             │
             ▼                             ▼
    ┌─────────────────┐           ┌─────────────────┐
    │      Pod 1      │           │      Pod 2      │
    │                 │           │                 │
    │ Flask Container │           │ Flask Container │
    │    Port 5000    │           │    Port 5000    │
    └─────────────────┘           └─────────────────┘
```

The Kubernetes Deployment runs **2 replicas** of the Flask application.

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **HTML/CSS**
- **Docker**
- **Kubernetes**
- **Minikube**
- **kubectl**

---

## 📁 Project Structure

```text
kubernetes_app/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── deployment.yaml
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 🌐 Application

The application contains a simple form:

```text
Kubernetes Test Application

Enter your name:
[________________]

Enter your email:
[________________]

        [ Submit ]
```

After submitting the form, the application displays a confirmation message containing the submitted name and email.

---

# 🐳 Docker

The application is packaged into a Docker image using the following Dockerfile:

```dockerfile
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
COPY app.py /app/
COPY templates /app/templates
COPY static /app/static

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
```

### Build the Docker Image

```bash
docker build -t kubernetes-test-app:latest .
```

Check the image:

```bash
docker images
```

---

# ☸️ Kubernetes Configuration

The project uses a Kubernetes **Deployment** and **Service**.

## Deployment

The Deployment creates two replicas:

```yaml
replicas: 2
```

Each Pod runs the Flask application on port `5000`.

The container uses:

```yaml
imagePullPolicy: Never
```

This is useful when working with a locally available Docker image in Minikube.

---

## Service

The Service exposes the application through port `8080` and forwards traffic to the Flask application running on port `5000`.

```yaml
ports:
  - port: 8080
    targetPort: 5000
```

The flow is:

```text
Service :8080
      ↓
Pod :5000
      ↓
Flask Application
```

---

# 🧊 Running with Minikube

## 1. Start Minikube

```bash
minikube start
```

Check the cluster:

```bash
minikube status
```

---

## 2. Use Minikube's Docker Environment

Because the Kubernetes Deployment uses:

```yaml
imagePullPolicy: Never
```

the Docker image needs to be available to Minikube.

Run:

```bash
minikube docker-env
```

Then configure your terminal to use Minikube's Docker daemon.

On PowerShell:

```powershell
minikube docker-env --shell powershell | Invoke-Expression
```

Now build the image:

```powershell
docker build -t kubernetes-test-app:latest .
```

Verify:

```powershell
docker images
```

---

## 3. Deploy the Application

Apply the Kubernetes configuration:

```bash
kubectl apply -f deployment.yaml
```

You should see something similar to:

```text
deployment.apps/kubernetes-test-app created
service/kubernetes-test-app created
```

---

# 🔍 Check Kubernetes Resources

### Check Deployment

```bash
kubectl get deployments
```

### Check Pods

```bash
kubectl get pods
```

Expected:

```text
NAME                                  READY   STATUS    RESTARTS
kubernetes-test-app-xxxxxxxxxx-xxxxx  1/1     Running   0
kubernetes-test-app-xxxxxxxxxx-xxxxx  1/1     Running   0
```

### Check Services

```bash
kubectl get services
```

### Get More Information

```bash
kubectl describe deployment kubernetes-test-app
```

For a Pod:

```bash
kubectl describe pod <pod-name>
```

---

# 🌍 Access the Application

Since this project uses Minikube, you can access the Service using:

```bash
minikube service kubernetes-test-app
```

Minikube will provide the URL and can open the application in your browser.

You can also check the Service URL using:

```bash
minikube service kubernetes-test-app --url
```

---

# 📊 Kubernetes Resources

The project contains:

| Resource | Purpose |
|---|---|
| Deployment | Manages the application Pods |
| Pod | Runs the Flask container |
| Service | Provides network access to the Pods |
| Minikube | Runs Kubernetes locally |
| Docker | Builds the application container |
| kubectl | Communicates with Kubernetes |

---

# 🔄 Application Flow

```text
1. User opens the website
          ↓
2. Request reaches Kubernetes Service
          ↓
3. Service forwards request to a Pod
          ↓
4. Flask application receives request
          ↓
5. User submits name and email
          ↓
6. Flask processes the POST request
          ↓
7. Confirmation message is displayed
```

---

# 📚 What I Learned

Through this project, I practiced the basic Kubernetes workflow:

```text
Application
    ↓
Dockerfile
    ↓
Docker Image
    ↓
Kubernetes Deployment
    ↓
Pods
    ↓
Kubernetes Service
    ↓
Minikube
    ↓
Application
```

### Kubernetes concepts practiced

- Pods
- Deployments
- Replica management
- Services
- Container ports
- Target ports
- Labels and selectors
- Image pull policies
- Resource requests and limits
- `kubectl`
- Minikube
- Local Kubernetes development

---

# 🧹 Cleanup

To remove the Kubernetes resources:

```bash
kubectl delete -f deployment.yaml
```

To stop Minikube:

```bash
minikube stop
```

To completely remove the Minikube cluster:

```bash
minikube delete
```

---

# 🎯 Future Improvements

Possible improvements for this project:

- Add persistent database storage
- Add ConfigMaps and Secrets
- Add Ingress
- Add Kubernetes Horizontal Pod Autoscaler
- Add health checks using liveness and readiness probes
- Push the Docker image to Docker Hub
- Deploy to a cloud Kubernetes cluster such as Amazon EKS
- Add CI/CD using GitHub Actions
- Add monitoring and logging

---

## 👨‍💻 Author

**Nikhil Kant**

BTech – Computer Science & Engineering

This project was created as part of my hands-on learning journey with **Docker, Kubernetes, and Minikube**.