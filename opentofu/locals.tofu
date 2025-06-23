locals {
  common_tags = {
    project = "blog"
  }
  env = {
    for tuple in regexall("(.*)=(.*)", file("../.env")) : tuple[0] => sensitive(tuple[1])
  }
}

