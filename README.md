# Terraform: Sample Lambda with Internet Access via Private Subnet & NAT Gateway

In this project, I create a Lambda function that retrieves an IP address by connecting to the ``api.ipify.org`` service.

The Lambda function code can be found in the ``src/`` directory.

## Prerequisites
1. Download and install [Terraform](https://developer.hashicorp.com/terraform/install)
2. Ensure you have AWS CLI installed and configured with appropriate access keys

## How to use
1. Modify ``provider.tf`` file to ensure Terraform can work with your AWS access key. For example, you might use a custom AWS profile.
2. Install Terraform dependencies with ``terraform init`` command.
3. Run the ``./prepare-files.sh`` script to zip Python script files. The files will be saved into the hidden ``./files`` directory.
4. Run ``terraform apply`` to create all AWS infrastructure for this project: Lambda functions, API Gateway, and DynamoDB table.
5. Run ``./test-api-gw.sh`` to create a record in DynamoDB, dump it, and remove it.
6. Destroy infrustreucture with ``terraform destroy``

## All the steps together except the first one:
```
terraform init
./prepare-files.sh
terraform apply -auto-approve
./test-lambda.sh
terraform destroy -auto-approve
```

## Example output
```
Public IP Address: 18.232.219.151
```
