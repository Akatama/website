resource "aws_s3_bucket" "ebs" {
  bucket = var.ebs_bucket_name
  tags   = local.common_tags
}

data "template_file" "ebs_config" {
  template = file("${path.module}/Dockerrun.aws.json.tpl")
  vars = {
    image_name = aws_ecr_repository.blog.repository_url
  }
}

resource "local_file" "ebs_config" {
  content  = data.template_file.ebs_config.rendered
  filename = "${path.module}/Dockerrun.aws.json"
}

resource "aws_s3_object" "ebs_deployment" {
  depends_on = [local_file.ebs_config]
  bucket     = aws_s3_bucket.ebs.id
  key        = "Dockerrun.aws.json"
  source     = "${path.module}/Dockerrun.aws.json"
  lifecycle {
    replace_triggered_by = [local_file.ebs_config]
  }
}
