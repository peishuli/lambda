
resource "aws_lambda_function" "lambda" {
  filename      = data.archive_file.zip.output_path
  function_name = "demo_function"
  role          = aws_iam_role.lambda_role.arn
  handler       = "app.lambda_handler"

  source_code_hash = data.archive_file.zip.output_base64sha256

  runtime = "python3.8"
}

data "archive_file" "zip" {
  type        = "zip"
  source_file = "${path.module}/../lambda/app.py"
  output_path = "${path.module}/output/app.zip"
}