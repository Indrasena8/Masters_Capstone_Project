# Cloud Native Application Development & Deployment Model: A Comparative Study

This repository contains the implementation and report for the capstone project: **Comparative Study of Cloud Native Application Development & Deployment Model**. The project explores the development and deployment of a cloud-native spam email detection application using Azure Kubernetes Service (AKS) and automation with Azure Functions.

## Table of Contents
- [Introduction](#introduction)
- [Project Architecture](#project-architecture)
- [Technologies Used](#technologies-used)
- [Deployment Steps](#deployment-steps)
  - [Phase 1: Kubernetes Deployment](#phase-1-kubernetes-deployment)
  - [Phase 2: Azure Functions Automation](#phase-2-azure-functions-automation)
- [Vulnerability Analysis](#vulnerability-analysis)
- [Evaluation](#evaluation)
- [Hosting](#hosting)
- [Future Work](#future-work)
- [References](#references)

---

## Introduction

Cloud-native applications transform software development by utilizing cloud platforms' scalability and efficiency. This project demonstrates these concepts by building a spam email detection application. The application leverages Kubernetes for initial deployment and Azure Functions for automating updates.

This repository includes:
- Source code for the spam detection application.
- Configuration files for Kubernetes deployment and Azure Functions.
- Detailed implementation and insights in the final report.

---

## Project Architecture

### Phase 1: Kubernetes Deployment
![Kubernetes Architecrure](https://github.com/Indrasena8/Masters_Capstone_Project/blob/main/Images/Phase1.png)

### Phase 2: Azure Functions Automation
![Azure Functions Architecture](https://github.com/Indrasena8/Masters_Capstone_Project/blob/main/Images/Phase2.png)

---

## Technologies Used

- **Kubernetes**: For container orchestration.
- **Docker**: For containerization.
- **Azure Kubernetes Service (AKS)**: Managed Kubernetes environment.
- **Azure Functions**: Serverless automation of workflows.
- **Azure Blob Storage**: Storage for datasets and models.
- **Python**: Backend for the spam detection application.
- **Flask**: API framework for serving predictions.
- **Nginx**: Load balancer for external access.

---

## Deployment Steps

### Phase 1: Kubernetes Deployment

1. **Containerize the Application**:
   - Dockerize the spam detection application.
   - Push the container image to Azure Container Registry (ACR).

2. **Deploy to AKS**:
   - Create a Kubernetes cluster using AKS.
   - Deploy the application using Kubernetes `Deployment` and `Service` YAML files.

3. **Host and Test the Application**:
   - Expose the service externally using Nginx.
   - Verify predictions through the HTTP API.

### Phase 2: Azure Functions Automation

1. **Automate Model Updates**:
   - Use Azure Functions for event-driven retraining of the model.
   - Trigger retraining upon dataset updates in Azure Blob Storage.

2. **Deploy Functions**:
   - Deploy `PredictFunction` to handle API requests.
   - Deploy `RetrainFunction` to automate the retraining pipeline.

3. **Test the Pipeline**:
   - Simulate dataset updates and verify automated retraining.
   - Validate predictions through the updated model.

---

## Vulnerability Analysis

Identified potential security risks and proposed mitigations:
- **Unsecured HTTP Access**: Use HTTPS with TLS certificates.
- **Hardcoded Secrets**: Store sensitive credentials in Azure Key Vault or Kubernetes Secrets.
- **Container Privileges**: Use a non-root user in the Docker container.
- **Input Validation**: Validate and sanitize inputs to prevent injection attacks.

For a detailed analysis, refer to the [Vulnerability Analysis section](https://github.com/Indrasena8/Masters_Capstone_Project/blob/main/Report/Indrasena_Final_Report.pdf) in the report.

---

## Evaluation

- Achieved **98% accuracy** on the spam detection model.
- Average response time: **200ms per prediction**.
- Seamless automation using Azure Functions minimized manual intervention.
- Reliable hosting and API access:
  - **Predict API**: [https://spamemaildetection.azurewebsites.net/api/predict](https://spamemaildetection.azurewebsites.net/api/predict)
  - **Hosted Application**: [http://172.210.63.81](http://172.210.63.81)

---

## Hosting

- The application is live at [http://172.210.63.81](http://172.210.63.81).
- Predict API endpoint: [https://spamemaildetection.azurewebsites.net/api/predict](https://spamemaildetection.azurewebsites.net/api/predict).

---

## Future Work

- **Comparison of Cloud Providers**: Evaluate similar workloads on AWS, Azure, and GCP.
- **Security Enhancements**: Implement all identified mitigations.
- **Scaling Workflows**: Extend to multi-service architectures using Kubernetes.

---

## References

1. [Azure Kubernetes Service (AKS) Documentation](https://learn.microsoft.com/en-us/azure/aks/)
2. [Azure Functions Documentation](https://learn.microsoft.com/en-us/azure/azure-functions/)
3. [Introduction to Kubernetes](https://trainingportal.linuxfoundation.org/learn/course/introduction-to-kubernetes)
4. [Serverless on Kubernetes](https://trainingportal.linuxfoundation.org/learn/course/introduction-to-serverless-on-kubernetes-lfs157)
5. [AI/ML Toolkits with Kubeflow](https://training.linuxfoundation.org/training/introduction-to-ai-ml-toolkits-with-kubeflow-lfs147)

---

## How to Use This Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cloud-native-application.git
2.	Follow the instructions in the report/Capstone_Final_Report.md for implementation details.
3.	Deploy the application using the provided configuration files in the deployment/ folder.
