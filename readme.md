# Cloud DevOps Engineer Capstone Project

This project represents the successful completion of the last final Capstone project and the Cloud DevOps Engineer Nanodegree at Udacity.

## What did I learn?

In this project, I applied the skills and knowledge I developed throughout the Cloud DevOps Nanodegree program. These include:
- Using Circle CI to implement Continuous Integration and Continuous Deployment
- Building pipelines
- Working with Ansible and CloudFormation to deploy clusters
- Building Kubernetes clusters
- Building Docker containers in pipelines
- Working in AWS

## Application

The Application is based on a python3 script using <a target="_blank" href="https://flask.palletsprojects.com">flask</a> to render a simple webpage in the user's browser.
A requirements.txt is used to ensure that all needed dependencies come along with the Application.

## Kubernetes Cluster

I used AWS CloudFormation to deploy the Kubernetes Cluster.
The CloudFormation Deployment can be broken down into four Parts:
- **Networking**, to ensure new nodes can communicate with the Cluster
- **Elastic Kubernetes Service (EKS)** is used to create a Kubernetes Cluster
- **NodeGroup**, each NodeGroup has a set of rules to define how instances are operated and created for the EKS-Cluster
- **Management** is needed to configure and manage the Cluster and its deployments and services. I created two management hosts for extra redundancy if one of them fails.

#### List of deployed Stacks:
![CloudFormation](./screenshots/cloudformation_stacks.PNG)

#### List of deployed Instances:
![Show Instances](./screenshots/show_instances.PNG)

## CircleCi - CI/CD Pipelines

I used CircleCi to create a CI/CD Pipeline to test and deploy changes manually before they get deployed automatically to the Cluster using Ansible.

#### From Zero to Hero demonstration:

![CircleCi Pipeline](./screenshots/circleci_pipeline.PNG)

## Linting using Pylint and Hadolint

Linting is used to check if the Application and Dockerfile is syntactically correct.
This process makes sure that the code quality is always as good as possible.

#### This is the output when the step fails:

![Linting step fail](./screenshots/linting_step_fail.PNG)


#### This is the output when the step passes:

![Linting step fail](./screenshots/linting_step_success.PNG)

## Access the Application

After the EKS-Cluster has been successfully configured using Ansible within the CI/CD Pipeline, I checked the deployment and service as follows:

```
$ kubectl get deployments
NAME                          READY   UP-TO-DATE   AVAILABLE   AGE
capstone-project-deployment   4/4     4            4           68m

$ kubectl get services
NAME                       TYPE           CLUSTER-IP       EXTERNAL-IP                                                                  PORT(S)        AGE
capstone-project-service   LoadBalancer   10.100.240.221   a9d7166a2525d405db00907ffb57de4e-1479088191.eu-central-1.elb.amazonaws.com   80:32299/TCP   69m
kubernetes                 ClusterIP      10.100.0.1       <none>                                                                       443/TCP        80m
```

Public LB DNS: http://a9d7166a2525d405db00907ffb57de4e-1479088191.eu-central-1.elb.amazonaws.com

![Access LB DNS](./screenshots/access_lb_dns_demo.PNG)
