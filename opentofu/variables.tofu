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
