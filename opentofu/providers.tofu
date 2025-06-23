terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "2.5.3"
    }
    template = {
      source  = "hashicorp/template"
      version = "2.2.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-west-1"
}

provider "local" {

}

provider "template" {

}
