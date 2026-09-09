---
page_type: sample
languages:
  - python
products:
  - azure
  - azure-redis-cache
description: "This sample creates a multi-container application in an Azure Kubernetes Service (AKS) cluster."
---

# AKSFlow

> **An end-to-end GitOps pipeline that provisions Azure infrastructure with Terraform, builds and security-scans container images in GitHub Actions, and continuously deploys to AKS via ArgoCD — with full observability through Prometheus and Grafana.**

This project implements a complete DevOps lifecycle for deploying a containerized application to Azure Kubernetes Service (AKS), built entirely on Infrastructure as Code and GitOps principles. The Azure infrastructure — an AKS cluster and a private Azure Container Registry (ACR) — is provisioned declaratively with Terraform, making the entire environment reproducible from code. A CI pipeline in GitHub Actions builds the application's container image, scans it for vulnerabilities with Trivy, and pushes it to the ACR, authenticating to Azure through keyless OIDC federation with no stored secrets. Deployment follows a pull-based GitOps model: ArgoCD, running inside the cluster, continuously watches the Git repository, renders the application's Helm chart, and synchronizes the cluster to match the desired state — with the AKS nodes pulling images from the ACR via a least-privilege Managed Identity. Finally, Prometheus collects cluster and application metrics, which Grafana visualizes as live dashboards, providing observability into the running system.


## Architecture

```mermaid
flowchart TB
    dev([Developer]):::person
    user([End User]):::person

    subgraph gh[" GitHub "]
        repo["Git Repository<br/>Helm chart · Terraform · App manifest"]:::git
        actions["GitHub Actions Pipeline<br/>build → Trivy scan → push"]:::ci
    end

    tf["Terraform · IaC<br/>provisions infrastructure"]:::tf

    subgraph azure[" Microsoft Azure "]
        acr[("Azure Container Registry")]:::azure
        subgraph aks[" AKS Cluster "]
            argo["ArgoCD<br/>GitOps controller"]:::argo
            app["Application Pods<br/>Front-end + Redis"]:::app
            mon["Prometheus + Grafana<br/>monitoring"]:::mon
        end
    end

    dev -->|git push| repo
    repo -->|triggers| actions
    actions -->|"push image · OIDC auth"| acr
    tf -.->|terraform apply| aks
    tf -.->|terraform apply| acr
    repo -->|"watches / pulls · GitOps"| argo
    argo -->|deploys via Helm| app
    acr -->|"image pull · Managed Identity"| app
    mon -.->|scrapes metrics| app
    app -->|LoadBalancer · public IP| user

    classDef person fill:#eceff1,stroke:#455a64,color:#263238
    classDef git fill:#e3f2fd,stroke:#1976d2,color:#0d47a1
    classDef ci fill:#e0f2f1,stroke:#00897b,color:#004d40
    classDef azure fill:#e1f5fe,stroke:#0277bd,color:#01579b
    classDef argo fill:#fce4ec,stroke:#c2185b,color:#880e4f
    classDef app fill:#fff3e0,stroke:#ef6c00,color:#e65100
    classDef mon fill:#f3e5f5,stroke:#8e24aa,color:#4a148c
    classDef tf fill:#ede7f6,stroke:#5e35b1,color:#311b92
```

## Tech Stack

- **Cloud & IaC:** Azure (AKS, ACR, Entra ID), Terraform
- **Containers & Orchestration:** Docker, Kubernetes, Helm
- **CI/CD & GitOps:** GitHub Actions, ArgoCD, OIDC federation
- **Observability & Security:** Prometheus, Grafana, Trivy, Kubescape


## Highlights

- Fully reproducible infrastructure via Terraform with remote state
- Keyless CI/CD authentication using OIDC (no stored secrets)
- Pull-based GitOps deployment with ArgoCD self-healing
- Security scanning (Trivy) integrated as a pipeline gate
- Least-privilege image pulls via Managed Identity