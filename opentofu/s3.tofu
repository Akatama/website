resource "aws_s3_bucket" "ebs" {
  bucket = var.ebs_bucket_name
  tags   = local.common_tags
}

resource "aws_s3_bucket_versioning" "ebs_versioning" {
  bucket = aws_s3_bucket.ebs.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_object" "ebs_deployment" {
  bucket = aws_s3_bucket.ebs.id
  key    = "Dockerrun.aws.json"
  content = templatefile("${path.module}/Dockerrun.aws.json.tftpl", {
    image_name = aws_ecr_repository.blog.repository_url
    tag_name   = var.image_tag
    db_port    = var.db_port
  })
}
