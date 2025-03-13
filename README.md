# Cloud Computing Kubernetes Project

## Overview
This project is a **Kubernetes-based multi-service deployment**
It demonstrates container orchestration using **Kubernetes (K8s)**, deploying microservices with load balancing, persistent storage, and a reverse proxy.

## Features
- **Microservices Architecture**: Includes Stocks, Capital-Gains, Database (MongoDB), and NGINX for reverse proxy.
- **Kubernetes Deployments**: Each service is deployed in a **Kubernetes cluster** using `kind`.
- **Load Balancing**: Traffic is distributed across replicas using **Kubernetes Services**.
- **Persistent Storage**: Ensures data retention via **PersistentVolumes** and **PersistentVolumeClaims**.
- **Reverse Proxy**: Uses **NGINX** to manage routing between services.
