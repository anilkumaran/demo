resource "aws_s3_bucket" "demo-bucket" {
  bucket = "demo-aws-bucket-from-terraform-12342124"

  tags = {
    Name        = "demo-aws-bucket-from-terraform-12342124"
    app         = "demo-ecom-app"
  }
}