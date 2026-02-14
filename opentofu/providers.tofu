terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket       = "akatama-web"
    key          = "terraform.tfstate"
    region       = "us-west-1"
    use_lockfile = true
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-west-1"
}
