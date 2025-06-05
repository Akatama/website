variable "naming_prefix" {
  type        = string
  description = "Naming prefix for resources"
  default     = "blog"
}

variable "vpc_cidr_block" {
  type        = string
  description = "Base CIDR block for VPC"
  default     = "10.0.0.0/16"
}

variable "blog_cidr_block" {
  type    = string
  default = "10.0.1.0/24"
}

variable "db1_cidr_block" {
  type    = string
  default = "10.0.3.0/24"
}

variable "db2_cidr_block" {
  type    = string
  default = "10.0.4.0/24"
}

variable "map_public_ip_on_launch" {
  type        = bool
  description = "Map a public IP address for Subnet instances"
  default     = true
}

variable "db_port" {
  type        = number
  description = "The port to use for the database"
}

variable "db_username" {
  type        = string
  description = "Username for the database"
}

variable "db_password" {
  type        = string
  description = "Password for the database"
  sensitive   = true
}

variable "db_instance_class" {
  type        = string
  description = "Instance class for the database"
  default     = "db.t3.micro"
}

variable "db_name" {
  type        = string
  description = "Name of the database"
}

variable "db_storage" {
  type        = number
  description = "Size in gigabytes for the database"
  default     = 20
}

variable "ecr_name" {
  type        = string
  description = "Name of the ECR instance"
  default     = "blog_ecr"
}

variable "ebs_bucket_name" {
  type        = string
  description = "The name of the s3 bucket used for EBS"
  default     = "ebs-blog-bucket"
}

variable "ebs_name" {
  type        = string
  description = "The name of the Elastic Beanstalk App"
  default     = "ebs_blog"
}

variable "blog_instance_class" {
  type        = string
  description = "Instance class for my blog"
  default     = "t3.micro"
}
