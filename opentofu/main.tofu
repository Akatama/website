resource "aws_elastic_beanstalk_application" "app" {
  name = var.ebs_name
  tags = local.common_tags

  appversion_lifecycle {
    service_role          = aws_iam_role.ebs.arn
    max_count             = 2
    delete_source_from_s3 = false
  }
}

resource "aws_elastic_beanstalk_application_version" "app_version" {
  name        = "${var.ebs_name}-version-${var.ebs_app_version_number - 1}"
  application = aws_elastic_beanstalk_application.app.name
  bucket      = aws_s3_bucket.ebs.id
  key         = aws_s3_object.ebs_deployment.id
  tags        = local.common_tags
}

# # This is the previous app version
resource "aws_elastic_beanstalk_application_version" "app_version_2" {
  name        = "${var.ebs_name}-version-${var.ebs_app_version_number}"
  application = aws_elastic_beanstalk_application.app.name
  bucket      = aws_s3_bucket.ebs.id
  key         = aws_s3_object.ebs_deployment.id
  tags        = local.common_tags
}

data "aws_acm_certificate" "domain" {
  domain      = var.domain_name
  types       = ["AMAZON_ISSUED"]
  most_recent = true
}

resource "aws_elastic_beanstalk_environment" "env" {
  name                   = "ebs-blog-env"
  application            = aws_elastic_beanstalk_application.app.name
  version_label          = aws_elastic_beanstalk_application_version.app_version_2.name
  solution_stack_name    = "64bit Amazon Linux 2023 v4.5.2 running Docker"
  tier                   = "WebServer"
  wait_for_ready_timeout = "10m"
  tags                   = local.common_tags

  setting {
    name      = "IamInstanceProfile"
    namespace = "aws:autoscaling:launchconfiguration"
    value     = aws_iam_instance_profile.beanstalk_iam_instance_profile.arn
  }

  setting {
    name      = "EnvironmentType"
    namespace = "aws:elasticbeanstalk:environment"
    value     = "LoadBalanced"
  }

  setting {
    name      = "MaxSize"
    namespace = "aws:autoscaling:asg"
    value     = 1
  }

  setting {
    name      = "SecurityGroups"
    namespace = "aws:autoscaling:launchconfiguration"
    value     = join("", [aws_security_group.blog_security.id])
  }

  setting {
    name      = "InstanceTypes"
    namespace = "aws:ec2:instances"
    value     = var.blog_instance_class
  }

  setting {
    name      = "VPCId"
    namespace = "aws:ec2:vpc"
    value     = aws_vpc.blog.id
  }

  setting {
    name      = "Subnets"
    namespace = "aws:ec2:vpc"
    value     = join("", [aws_subnet.blog.id])
  }

  setting {
    name      = "ListenerProtocol"
    namespace = "aws:elb:listener:443"
    value     = "HTTPS"
  }

  setting {
    name      = "InstancePort"
    namespace = "aws:elb:listener:443"
    value     = "80"
  }

  setting {
    name      = "SSLCertificateId"
    namespace = "aws:elb:listener:443"
    value     = data.aws_acm_certificate.domain.arn
  }

  setting {
    name      = "ListenerEnabled"
    namespace = "aws:elb:listener"
    value     = false
  }

  setting {
    name      = "DJANGO_ALLOWED_HOSTS"
    namespace = "aws:elasticbeanstalk:application:environment"
    value     = var.django_allowed_hosts
  }

  setting {
    name      = "DJANGO_LOGLEVEL"
    namespace = "aws:elasticbeanstalk:application:environment"
    value     = var.django_loglevel
  }

  setting {
    name      = "RDS_DB_NAME"
    namespace = "aws:elasticbeanstalk:application:environment"
    value     = var.db_name
  }

  setting {
    name      = "RDS_HOSTNAME"
    namespace = "aws:elasticbeanstalk:application:environment"
    value     = aws_db_instance.blog_db.address
  }

  setting {
    name      = "RDS_PORT"
    namespace = "aws:elasticbeanstalk:application:environment"
    value     = var.db_port
  }

  setting {
    name      = "RDS_USERNAME"
    namespace = "aws:elasticbeanstalk:application:environment"
    value     = var.db_username
  }

  setting {
    name      = "RDS_PASSWORD"
    namespace = "aws:elasticbeanstalk:application:environment"
    value     = var.db_password
  }

  setting {
    name      = "SECRET_KEY"
    namespace = "aws:elasticbeanstalk:application:environment"
    value     = var.secret_key
  }

}
