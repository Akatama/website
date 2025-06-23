resource "aws_db_subnet_group" "db_group" {
  name       = "${var.naming_prefix}_db_subnet_group"
  subnet_ids = [aws_subnet.db1.id, aws_subnet.db2.id]
  tags       = local.common_tags
}

resource "aws_db_instance" "blog_db" {
  allocated_storage      = var.db_storage
  db_name                = var.db_name
  engine                 = "postgres"
  engine_version         = "17.4"
  instance_class         = var.db_instance_class
  username               = var.db_username
  password               = var.db_password
  db_subnet_group_name   = resource.aws_db_subnet_group.db_group.name
  port                   = var.db_port
  vpc_security_group_ids = [aws_security_group.db_security.id]
  publicly_accessible    = false
  tags                   = local.common_tags
}
