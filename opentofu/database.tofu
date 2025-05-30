resource "aws_db_subnet_group" "db_group" {
  name       = "${var.naming_prefix}_db_subnet_group"
  subnet_ids = [for _, value in module.vpc.private_subnet_attributes_by_az : value.id]
  tags       = locals.common_tags
}

resource "aws_db_instance" "blog_db" {
  allocated_storage    = var.db_storage
  db_name              = var.db_name
  engine               = "postgres"
  engine_version       = "17.4"
  instance_class       = var.instance_class
  username             = var.username
  password             = var.password
  db_subnet_group_name = resource.aws_db_subnet_group.db_group.name
  port                 = var.db_port
}
