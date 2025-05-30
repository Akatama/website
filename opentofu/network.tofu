module "vpc" {
  source  = "aws-ia/vpc/aws"
  version = ">= 4.2.0"

  name                                 = "${var.naming_prefix}-vpc"
  cidr_block                           = var.vpc_cidr_block
  vpc_assign_generated_ipv6_cidr_block = false
  vpc_egress_only_internet_gateway     = false
  az_count                             = 2
  tags                                 = locals.common_tags

  subnets = {
    private_db = {
      name_prefix               = "db"
      netmask                   = 24
      assign_ipv6_cidr          = false
      nat_gateway_configuration = "none"
    }
    private_db2 = {
      name_prefix               = "db2"
      netmask                   = 24
      assign_ipv6_cidr          = false
      nat_gateway_configuration = "none"
    }
    public = {
      name_prefix               = "blog"
      netmask                   = 24
      assign_ipv6_cidr          = false
      nat_gateway_configuration = "none"
      map_public_ip_on_launch   = var.map_public_ip_on_launch
    }
    public2 = {
      name_prefix               = "blog2"
      netmask                   = 24
      assign_ipv6_cidr          = false
      nat_gateway_configuration = "none"
      map_public_ip_on_launch   = var.map_public_ip_on_launch
    }
  }
}

resource "aws_security_group" "blog_security" {
  name        = "${var.naming_prefix}_security"
  description = "Security group for my blog"
  vpc_id      = aws_vpc.main.id
  tags        = locals.common_tags
}

resource "aws_vpc_security_group_ingress_rule" "allow_tls" {
  security_group_id = aws_security_group.blog_security.id
  ip_protocol       = "tcp"
  from_port         = 443
  to_port           = 443
}

resource "aws_vpc_security_group_ingress_rule" "allow_http" {
  security_group_id = aws_security_group.blog_security.id
  ip_protocol       = "tcp"
  from_port         = 80
  to_port           = 80
}

resource "aws_security_group" "db_secuity" {
  name        = "${var.naming_prefix}_db_security"
  description = "Security group for database"
  vpc_id      = model.vpc.vpc_id
  tags        = locals.common_tags
}

resource "aws_vpc_security_group_ingress_rule" "allow_db_connection" {
  security_group_id = aws_security_group.db_secuity.id
  from_port         = var.db_port
  to_port           = var.db_port
  ip_protocol       = "tcp"
}
