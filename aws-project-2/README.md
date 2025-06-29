# Host Static Website with S3 & CloudFront

## 🎯 Objective
Host static content using S3 and deliver globally via CloudFront.

## 🛠 Tools & Technologies
- Amazon S3
- CloudFront

## ✅ Expected Output
A fast, CDN-delivered static website.

## 🌐 Live Website 
This site is part of my RISE Internship project, hosted on Amazon S3 and delivered using CloudFront for high-speed global access. A fully serverless and scalable deployment.

via CloudFront CDN -> [https://d3q2vue2f863z6.cloudfront.nett](https://d3q2vue2f863z6.cloudfront.net)  
via Amazon S3 -> [https://rise-project2-pragnya.s3.ap-south-1.amazonaws.com/index.html](https://rise-project2-pragnya.s3.ap-south-1.amazonaws.com/index.html)  

## 📸 Screenshot
![Preview](../images/project-2.png)
![Preview](../images/project-2%20bucket.png)
![Preview](../images/project-2%20cloudfront.png)

## 📹 Video explanation
[Click here to view the screen recording](https://drive.google.com/file/d/1Bb-LEMoQclnpKDt8ahLtrXMjT2VuWIo-/view?usp=sharing)

## 🔄 How It Works
A static website was hosted using an AWS S3 bucket configured for static website hosting. The website files were uploaded and made publicly accessible. CloudFront was added as a CDN (Content Delivery Network) to distribute the site globally with improved performance and security. This setup eliminated the need for servers while ensuring high availability.

## 🧠 What I Learned
- How to configure and host websites using S3 buckets
- Writing and applying bucket policies for public access
- How CloudFront distributions cache and serve static assets
- Understanding website endpoints vs. S3 URLs
- Deploying cost-efficient and serverless websites on AWS