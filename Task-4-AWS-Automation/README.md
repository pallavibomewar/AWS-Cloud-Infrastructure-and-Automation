# Task 4 – AWS EC2 Automation Script

## Objective
Create a Python automation script to list running Amazon EC2 instances, filter them by environment tag, and generate an estimated monthly cost summary.

## Technologies Used
- Python 3
- AWS Boto3 SDK
- Amazon EC2
- AWS CloudShell
- GitHub

## Implementation Steps
1. Created the `ec2_report.py` Python script.
2. Used Boto3 to connect to Amazon EC2.
3. Filtered instances with the `running` state and `Environment=dev` tag.
4. Added example hourly rates for selected EC2 instance types.
5. Calculated estimated monthly costs using 730 hours per month.
6. Executed and tested the script using AWS CloudShell.

## Run the Script

```bash
python3 ec2_report.py
```

## Test Result

```text
Development EC2 Instance Report
--------------------------------
No running development EC2 instances found.
Total Estimated Monthly Cost: $0.00
```

The script executed successfully. No matching running EC2 instances were found in the selected AWS Region.

## Limitations
- Hourly rates are illustrative, not live AWS pricing.
- The estimate excludes storage, data transfer, taxes, and other AWS charges.
- No matching running development EC2 instance was available for testing.
- Testing was performed in a personal AWS account, not the company development environment.

## Conclusion
Successfully created and tested a Python-based EC2 reporting script using AWS Boto3.
