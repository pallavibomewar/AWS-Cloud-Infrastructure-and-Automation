# Task 2 – AWS Infrastructure Architecture

## Objective
To understand and document the existing AWS infrastructure and static website deployment.

## AWS Region
Europe (Stockholm) – eu-north-1

## Infrastructure Overview
I reviewed the existing AWS resources and created an architecture diagram.

### VPC Configuration
- VPC ID: `vpc-0cb400a1d428c544d`
- VPC CIDR: `172.31.0.0/16`
- Subnets: 3
- Route Table: `rtb-089a6d30df50b25af`
- Internet Gateway: `igw-0eec1e8157ae7d2ef`

### Subnet Details

| Subnet | CIDR | Availability Zone |
|---|---|---|
| subnet-05c7a8d2fe0b9a3f3 | 172.31.0.0/20 | eu-north-1c |
| subnet-0cb6ebcddd519fb61 | 172.31.32.0/20 | eu-north-1b |
| subnet-0640d9558ef82561d | 172.31.16.0/20 | eu-north-1a |

## Static Website Architecture
I deployed a static website using Amazon S3 and CloudFront.

Website flow:

User → CloudFront → Amazon S3 → index.html

CloudFront uses Origin Access Control (OAC) to access the S3 bucket securely.

## Architecture Diagram

![AWS Architecture](aws_architecture.png)


