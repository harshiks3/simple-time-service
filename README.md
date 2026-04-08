# SimpleTimeService

## 1. Overview

SimpleTimeService is a lightweight Python-based microservice that returns the current timestamp and the client’s IP address in JSON format.

The application is containerized using Docker and deployed to AWS using Infrastructure as Code (Terraform) on ECS Fargate, following best practices for networking, security, and scalability.

---

## 2. Features

* Returns current UTC timestamp and client IP
* Stateless microservice design
* Containerized using Docker
* Runs as a non-root user for enhanced security
* Deployed on AWS ECS Fargate
* Accessible via Application Load Balancer
* Infrastructure fully provisioned using Terraform

---

## 3. Technology Stack

* Language: Python (Flask)
* Containerization: Docker
* Cloud Platform: AWS
* Compute: ECS Fargate
* Networking: VPC (Public and Private Subnets)
* Load Balancing: Application Load Balancer (ALB)
* Infrastructure as Code: Terraform

---

## 4. Architecture

[Architecture Diagram](docs/architecture.png)

This diagram illustrates the end-to-end deployment of the application using AWS ECS Fargate, Application Load Balancer, and Terraform-managed infrastructure.

The application is deployed using a secure and scalable cloud-native architecture:

* A custom VPC with public and private subnets across multiple Availability Zones
* Application Load Balancer (ALB) deployed in public subnets
* ECS Fargate service deployed in private subnets
* NAT Gateway to allow outbound internet access for private resources
* Security groups configured to allow only required traffic between components

Traffic Flow:

Client → ALB (Public Subnet) → ECS Fargate Service (Private Subnet)

---

## 5. Prerequisites

Ensure the following tools are installed and configured:

* AWS CLI (with valid credentials and permissions)
* Terraform (v1.0 or later recommended)
* Docker

---

## 6. Setup and Deployment

### 6.1 Build and Push Docker Image

Navigate to the application directory:

cd app

Build the Docker image:

docker build -t <your-dockerhub-username>/simple-time-service .

Push the image to Docker Hub:

docker push <your-dockerhub-username>/simple-time-service

Update the image reference in:

terraform/terraform.tfvars

---

### 6.2 Deploy Infrastructure Using Terraform

Navigate to the Terraform directory:

cd terraform

Initialize Terraform:

terraform init

Review the execution plan:

terraform plan

Apply the configuration:

terraform apply

---

## 7. Accessing the Application

After successful deployment, retrieve the Application Load Balancer DNS:

terraform output alb_dns_name

Open the following in your browser:

http://simple-time-service-alb-1748285863.ap-south-1.elb.amazonaws.com/

Example response:

{
"timestamp": "2026-04-08T06:49:48.857015",
"ip": "x.x.x.x"
}

http://simple-time-service-alb-1748285863.ap-south-1.elb.amazonaws.com/health

Example response:

{
  "status": "healthy"
}
---

## 8. Security Considerations

* The container runs as a non-root user
* Application is deployed in private subnets
* Only the load balancer is exposed to the internet
* Security groups restrict access between ALB and ECS tasks
* No sensitive credentials are stored in the repository

---

## 9. Cleanup

To destroy all provisioned resources:

terraform destroy

---

## 10. Notes

* Deployment may take several minutes due to infrastructure provisioning
* Health checks are configured to ensure application availability


