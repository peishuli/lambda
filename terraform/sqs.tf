resource "aws_sqs_queue" "sqs" {
  name = "lambda"
  tags = {
    Environment = "dev"
  }
}

