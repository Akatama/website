resource "aws_ecr_repository" "blog" {
  name                 = var.ecr_name
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
  encryption_configuration {
    encryption_type = "AES256"
  }
  tags = local.common_tags
}

resource "aws_ecr_lifecycle_policy" "example" {
  repository = aws_ecr_repository.blog.name

  policy = <<EOF
{
  "rules": [
    {
      "rulePriority": 1,
      "description": "Keep last 50 images",
      "selection": {
        "tagStatus": "tagged",
        "tagPatternList": ["*"],
        "countType": "imageCountMoreThan",
        "countNumber": 50
      },
      "action": {
        "type": "expire"
      }
    }
  ]
}
EOF
}
