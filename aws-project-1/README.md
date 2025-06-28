# Deploy Website on AWS EC2

## 🎯 Objective
Launch a Linux EC2 instance, install a web server (Apache/Nginx),
and host a basic HTML/CSS website.

## 🔧 Tools Used
- AWS EC2 (Free Tier)
- Ubuntu 22.04
- Apache
- Git & GitHub

## 🌐 Live Website
Deployed at: `http://<ec2-ip-address>`

## Screenshots
Here’s how the live website looks on EC2:  
(*To ensure cost-efficiency, I deactivated the EC2 instance used for Project 1 immediately after its completion.*)
![Preview](../images/project-1.png)
![Preview](../images/project-1%20instances.png)

## 🔄 How It Works
This project involves launching a Linux-based EC2 instance on AWS and hosting a static HTML/CSS website using Apache. The EC2 instance acts as a remote server that can serve web content globally over the internet. After configuring the security group and web server, the site becomes publicly accessible through the instance's public IP address.

## 🧠 What I Learned
- How to create and configure an AWS EC2 instance
- Basics of Linux terminal commands and remote access using SSH
- How Apache works as a web server
- Hosting and updating static websites from the cloud