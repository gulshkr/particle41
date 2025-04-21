# SimpleTimeService Infrastructure

Terraform configuration to deploy SimpleTimeService on AWS ECS Fargate.

## Prerequisites

1. AWS account with sufficient permissions
2. Terraform installed (v1.0+)
3. AWS CLI configured with credentials

## Deployment Instructions

1. Initialize Terraform:
```bash
terraform init
```
2. Review execution plan:
```
terraform plan
```
3. Apply configuration:
```
terraform apply
```
4. After deployment completes, access the service at:
```
http://<alb_dns_name>
```
5. To destroy all resources:
```
terraform destroy
```