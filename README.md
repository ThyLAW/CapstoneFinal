# CapstoneFinal (WIP)

## Introduction
test

The goal is to simulate a real DevOps IT Infrastructure which is a methodology that is becoming [much more prevalent ](https://cloud.google.com/blog/products/devops-sre/announcing-dora-2021-accelerate-state-of-devops-report)

You can see weekly updates on the development of this project [here](https://lawsblog.me/)

## Description

This project will demonstrate simple vulnerable web application(s) being scanned and rejected by CI/CD pipeline through various testers and linters and then demonstrate a "fixed" application successfully being passed throughout the pipeline.

![9-21-21 Pipeline Plan](/9-21-21diagram.png)

### Tools Used

- **CI/CD**: Azure DevOps
- **Code Repository**: GitHub
- **Cloud Provider**: Microsoft Azure App Service
- **Container Registry**: Docker Hub, Microsoft Container Registry (Issue Shown [here](https://docs.microsoft.com/en-us/answers/questions/593633/azure-app-service-fails-to-start-docker-flask-can.html)
- **Containerization**: Docker
- **Monitoring**: DataDog, Microsoft Azure Monitoring & Alerts (WIP)
- **Notifications**: Slack (WIP), Teams (WIP), GitHub (WIP)
- **DevOps Collaboration**: Azure Boards (WIP)
- **Linters**: Hadolint (Dockerfile Linter)
- **SAST**: WhiteSource Bolt (Open Source Vulnerability Scanner)
- **DAST**: WIP
- **Other**: WIP

### Stretch Goal Tools

As per my [project proposal](https://lawsblog.me/posts/capstone-project-week-2-proposal/), the main goal of this project is your average CI/CD pipeline that automatically takes and builds code from a repository into a container and pushes it to a server. However, there are some optional features that I want to include:

- **Heavy SAST/DAST Scanning**: Shifting left is the name of the game nowadays and companies are introducing security into their pipeline as a requirement. While this is not one of the main goals, I definitely want to include a lot of testing into my pipeline if I get the chance. No plans or ideas for tools yet.
- **Container Orchestration**: Kubernetes is a really interesting technology and employers would love to see experience with it. If I have time, I would like to include kubernetes as an optional stretch goal.
- **Infrastructure as Code**: Terraform. If you automate application deployments, then why not automate the infrastructure you deploy to? Terraform would be another great addition to my project.

## Works Used

The application(s) utilized in this capstone is/are sourced from [skf-labs](https://github.com/blabla1337/skf-labs), which is a collection if **intentionally vulnerable web applications** using **Flask**. These applications are a good fit for my pipeline as they provide only a single vulnerability and documentation for resolution which will allow me to demonstrate me fixing the vulnerability!

My [original prototype](https://github.com/ThyLAW/CapstonePrototype) utilized [OWASP JuiceShop](https://github.com/juice-shop/juice-shop) but due to the size of the application, I will not be able to fix it, so I had to move on.
