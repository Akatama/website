resource "aws_iam_role" "ebs" {
  name = var.ebs_name

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "web_tier" {
  role       = aws_iam_role.ebs.name
  policy_arn = "arn:aws:iam::aws:policy/AWSElasticBeanstalkWebTier"
}

resource "aws_iam_role_policy_attachment" "worker_tier" {
  role       = aws_iam_role.ebs.name
  policy_arn = "arn:aws:iam::aws:policy/AWSElasticBeanstalkWorkerTier"
}

resource "aws_iam_policy" "ecr" {
  name        = "${var.naming_prefix}-ECRFullAccessPolicy"
  description = "Provides full access to Amazon Elastic Container Registry (ECR)"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = [
          "ecr:GetAuthorizationToken",
          "ecr:BatchCheckLayerAvailability",
          "ecr:GetDownloadUrlForLayer",
          "ecr:GetRepositoryPolicy",
          "ecr:DescribeRepositories",
          "ecr:ListImages",
          "ecr:BatchGetImage"
        ],
        Effect   = "Allow",
        Resource = aws_ecr_repository.blog.arn,
      },
      {
        Action = [
          "ecr:GetAuthorizationToken"
        ]
        Effect   = "Allow"
        Resource = "*"
      }
    ],
  })
}

resource "aws_iam_role_policy_attachment" "ecr" {
  role       = aws_iam_role.ebs.name
  policy_arn = aws_iam_policy.ecr.arn
}

resource "aws_iam_instance_profile" "beanstalk_iam_instance_profile" {
  name = "blog-beanstalk-iam-instance-profile"
  role = aws_iam_role.ebs.name
}
