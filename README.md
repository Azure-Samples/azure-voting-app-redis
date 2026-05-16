# Azure Voting App — DevOps Pipeline Project

A fully containerized application deployed to Azure Kubernetes Service (AKS) through automated CI/CD pipelines built with GitHub Actions and Azure DevOps. All infrastructure is provisioned as code using Terraform.

## Architecture
GitHub Repository
↓
CI/CD Pipeline (GitHub Actions / Azure DevOps)
↓
Docker Image → Azure Container Registry (ACR)
↓
Azure Kubernetes Service (AKS)
↓
Public Load Balancer → Live Application

## Tech Stack

- **Infrastructure as Code:** Terraform
- **Containerization:** Docker
- **Container Orchestration:** Kubernetes (AKS)
- **CI/CD:** GitHub Actions + Azure DevOps Pipelines
- **Container Registry:** Azure Container Registry (ACR)
- **Cloud Platform:** Microsoft Azure
- **Application:** Python Flask + Redis

## Infrastructure

All Azure infrastructure is provisioned using Terraform:

- **Resource Group** — contains all project resources
- **Azure Container Registry (ACR)** — stores Docker images tagged by commit SHA
- **Azure Kubernetes Service (AKS)** — single-node cluster running containerized workloads
- **Role Assignment** — grants AKS permission to pull images from ACR automatically

## CI/CD Pipeline

Both pipelines trigger automatically on every push to master and execute the following stages:

1. **Build** — builds a Docker image tagged with the commit SHA and pushes it to ACR
2. **Deploy** — updates the running AKS deployment with the new image and monitors rollout status

## Branch Protection

The master branch is protected. All changes must be submitted via pull request and the CI/CD pipeline must pass before merging is allowed.

## Local Setup

### Prerequisites
- Azure CLI
- Terraform
- Docker
- kubectl

### Deploy Infrastructure
```bash
cd terraform
terraform init
terraform apply
```

### Push Docker Image
```bash
az acr login --name diegogambaacr
docker build -t diegogambaacr.azurecr.io/azure-vote-front:v1 ./azure-vote
docker push diegogambaacr.azurecr.io/azure-vote-front:v1
```

### Deploy to Kubernetes
```bash
az aks get-credentials --resource-group devops-project-rg --name devops-aks-cluster
kubectl apply -f k8s/azure-vote-all-in-one-redis.yaml
```

### Destroy Infrastructure
```bash
cd terraform
terraform destroy
```

## Author

Diego Gamba — DevOps Engineer
[LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/DiegoGamba)