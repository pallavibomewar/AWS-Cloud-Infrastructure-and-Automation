# Task 1 – AWS Cloud Account Onboarding

## Objective
To understand AWS account access, IAM user management, and AWS CLI configuration.

## AWS Services Used
- AWS Identity and Access Management (IAM)
- AWS Management Console
- AWS CLI

## 1. IAM Configuration

I reviewed the IAM service and created an IAM group and a user for practice.

**IAM User:** `week1-dev-user`

I used an IAM user instead of root credentials for AWS CLI access.

## 2. AWS CLI Configuration

I installed AWS CLI on my Windows laptop and configured a named profile.

**AWS CLI Profile:** `week1-dev`

I verified the configuration using:

```bash
aws sts get-caller-identity --profile week1-dev
```

The command returned my AWS account identity and IAM user ARN, confirming that AWS CLI authentication was working.

## 3. MFA Configuration

I attempted to configure Multi-Factor Authentication (MFA) for additional account security.

However, I encountered a verification error during setup. MFA configuration is pending.

## 4. Verification

- IAM group created
- IAM user created
- AWS CLI installed and configured
- IAM user identity verified using AWS STS
- MFA setup attempted; verification pending

## 5. Conclusion

In this task, I learned how to manage IAM users and groups, configure AWS CLI, and verify AWS account access using the command line.
