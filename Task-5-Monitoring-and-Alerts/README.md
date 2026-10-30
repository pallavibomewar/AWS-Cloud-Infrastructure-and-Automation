# Week 1 – Cloud Monitoring and Cost Alerts

## Project Overview

This project demonstrates basic AWS monitoring and cost management using Amazon EC2, Amazon CloudWatch, and AWS Budgets.

The objective is to monitor EC2 CPU utilization and track AWS spending using a monthly budget.

## 1. EC2 Instance Setup

Created an EC2 instance for monitoring.

| Configuration | Details |
|---|---|
| Instance Name | week-1-monitoring-ec2 |
| Instance ID | i-08d7bea1a008ad53e |
| Instance Status | Running |
| Monitoring Service | Amazon CloudWatch |

## 2. CPU Utilization Monitoring

Used Amazon CloudWatch to monitor EC2 CPU utilization.

**Metric Configuration:**

- Namespace: AWS/EC2
- Metric: CPUUtilization
- Statistic: Average
- Period: 5 Minutes
- Threshold: 70%
- Condition: Greater than 70%

The purpose is to monitor CPU usage and identify high resource utilization.

## 3. AWS Cost Monitoring

Created a monthly cost budget using AWS Billing and Cost Management.

**Budget Configuration:**

| Configuration | Value |
|---|---|
| Budget Name | week1-cost-alert |
| Budget Type | Monthly Cost Budget |
| Budget Amount | $1.00 |
| Alert Threshold | Actual Cost > $0.01 |
| Current Amount Used | $0.00 |

The budget helps track AWS spending and monitor costs.

## 4. Services Used

- Amazon EC2
- Amazon CloudWatch
- AWS Billing and Cost Management
- AWS Budgets

## 5. Learning Outcomes

- Learned how to launch and monitor an EC2 instance.
- Learned how to view CPU utilization metrics.
- Learned how to configure CloudWatch metric alarms.
- Learned how to create a monthly AWS budget.
- Understood the basics of cloud resource monitoring and cost management.

## 6. Conclusion

Successfully worked on AWS EC2 monitoring and cost management using CloudWatch and AWS Budgets.

This task provided practical knowledge of basic cloud infrastructure monitoring and cost optimization.
