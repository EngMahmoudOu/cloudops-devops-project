# CloudOps DevOps Project

An end-to-end DevOps project built around a Python Flask application, covering infrastructure automation, CI/CD, Kubernetes, GitOps, monitoring, logging, and security.

## Architecture

```text
                    GitHub
                   /      \
          GitHub Actions   Argo CD
                |             |
          Test / Trivy       Helm
                |             |
              Docker      Kubernetes
                              |
                         Flask Application

Terraform → AWS → EC2 → Ansible

Prometheus ─┐
            ├── Grafana
Alloy → Loki┘
```

## Tech Stack

Python · Flask · Docker · GitHub Actions · AWS · Terraform · Ansible · Kubernetes · Helm · Argo CD · Prometheus · Grafana · Loki · Alloy · Trivy

## What I Implemented

- Containerized a Flask application with Docker
- Built a CI pipeline with GitHub Actions and Trivy security scanning
- Provisioned AWS infrastructure using Terraform
- Automated EC2 configuration with Ansible
- Deployed and managed the application on Kubernetes
- Used Helm to manage Kubernetes configuration
- Implemented GitOps deployment and drift correction with Argo CD
- Set up metrics and logging with Prometheus, Grafana, Loki, and Alloy
- Tested Pod recovery, deployment failures, and configuration drift

## Project Structure

```text
app/          Flask application
terraform/    AWS infrastructure
ansible/      EC2 configuration
kubernetes/   Kubernetes manifests
helm/         Helm chart
.github/      CI workflow
```

This project was built to put the main DevOps components into one working environment and understand how they interact from code to deployment and monitoring.
