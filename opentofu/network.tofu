resource "aws_vpc" "blog" {
  cidr_block           = var.vpc_cidr_block
  tags                 = local.common_tags
  enable_dns_hostnames = true
}

resource "aws_subnet" "blog" {
  vpc_id                  = aws_vpc.blog.id
  tags                    = local.common_tags
  map_public_ip_on_launch = true
  cidr_block              = var.blog_cidr_block
  availability_zone       = "us-west-1a"
}

resource "aws_subnet" "db1" {
  vpc_id                  = aws_vpc.blog.id
  tags                    = local.common_tags
  map_public_ip_on_launch = false
  cidr_block              = var.db1_cidr_block
}

resource "aws_subnet" "db2" {
  vpc_id                  = aws_vpc.blog.id
  tags                    = local.common_tags
  map_public_ip_on_launch = false
  cidr_block              = var.db2_cidr_block
  availability_zone       = "us-west-1b"
}

resource "aws_security_group" "blog_security" {
  name        = "${var.naming_prefix}_security"
  description = "Security group for my blog"
  vpc_id      = aws_vpc.blog.id
  tags        = local.common_tags
}

resource "aws_vpc_security_group_ingress_rule" "allow_tls" {
  security_group_id = aws_security_group.blog_security.id
  ip_protocol       = "tcp"
  from_port         = 443
  to_port           = 443
  cidr_ipv4         = "0.0.0.0/0"
}

resource "aws_vpc_security_group_ingress_rule" "allow_http" {
  security_group_id = aws_security_group.blog_security.id
  ip_protocol       = "tcp"
  from_port         = 80
  to_port           = 80
  cidr_ipv4         = "0.0.0.0/0"
}

resource "aws_vpc_security_group_ingress_rule" "db_access" {
  security_group_id            = aws_security_group.blog_security.id
  ip_protocol                  = "tcp"
  from_port                    = var.db_port
  to_port                      = var.db_port
  referenced_security_group_id = aws_security_group.db_security.id
}

resource "aws_vpc_security_group_egress_rule" "db_access" {
  security_group_id            = aws_security_group.blog_security.id
  ip_protocol                  = "tcp"
  from_port                    = var.db_port
  to_port                      = var.db_port
  referenced_security_group_id = aws_security_group.db_security.id
}

resource "aws_security_group" "db_security" {
  name        = "${var.naming_prefix}_db_security"
  description = "Security group for database"
  vpc_id      = aws_vpc.blog.id
  tags        = local.common_tags
}

resource "aws_vpc_security_group_ingress_rule" "allow_db_connection" {
  security_group_id            = aws_security_group.db_security.id
  from_port                    = var.db_port
  to_port                      = var.db_port
  ip_protocol                  = "tcp"
  referenced_security_group_id = aws_security_group.blog_security.id
}

resource "aws_internet_gateway" "gateway" {
  vpc_id = aws_vpc.blog.id
  tags   = local.common_tags
}
