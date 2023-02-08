resource "aws_s3_bucket" "sourcefuss-nginx-bucket" {
  bucket = "sourcefuss-logs"
}

resource "aws_s3_bucket_policy" "allow_access_from_another_account" {
  bucket = aws_s3_bucket.sourcefuss-nginx-bucket.id
  policy = data.aws_iam_policy_document.allow_access_from_another_account.json
}

data "aws_iam_policy_document" "allow_access_from_another_account" {
  statement {
    principals {
      type        = "AWS"
      identifiers = ["AWS_ACCOUNT_ID"]
    }

    actions = [
      "s3:GetObject",
      "s3:ListBucket",
    ]

    resources = [
      aws_s3_bucket.sourcefuss-nginx-bucket.arn,
      "${aws_s3_bucket.sourcefuss-nginx-bucket.arn}/*",
    ]
  }
}
