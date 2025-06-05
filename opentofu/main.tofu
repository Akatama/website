resource "aws_elastic_beanstalk_application" "app" {
  name = var.ebs_name
  tags = local.common_tags
}

resource "aws_elastic_beanstalk_application_version" "app_version" {
  name        = "${var.ebs_name}-version"
  application = aws_elastic_beanstalk_application.app.name
  bucket      = aws_s3_bucket.ebs.id
  key         = aws_s3_object.ebs_deployment.id
  tags        = local.common_tags
}

resource "aws_elastic_beanstalk_environment" "env" {
  name                   = "ebs-blog-env"
  application            = aws_elastic_beanstalk_application.app.name
  version_label          = aws_elastic_beanstalk_application_version.app_version.name
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
    value     = "SingleInstance"
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

  # setting {
  #   name      = "SSLCertificateId"
  #   namespace = "aws:elb:loadbalancer"
  #   value     = aws_acm_certificate.cert.certificate_id
  # }
  #
  # dynamic "setting" {
  #   for_each = local.app_env
  #   content {
  #     namespace = "aws:elasticbeanstalk:application:environment"
  #     name      = setting.key
  #     value     = setting.value
  #   }
  # }
}
