resource "aws_lambda_event_source_mapping" "trigger" {
  event_source_arn = aws_sqs_queue.sqs.arn
  function_name    = aws_lambda_function.lambda.arn
}

resource "aws_cloudwatch_log_group" "lambda" {
  name = "/aws/lambda/${aws_lambda_function.lambda.function_name}"

  retention_in_days = 30
}