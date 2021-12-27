resource "aws_dynamodb_table" "dynamodb" {
  name           = "users"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "username"
  range_key      = "last_name"
  attribute {
    name = "username"
    type = "S"
  }
  attribute {
    name = "last_name"
    type = "S"
  }

  tags = {
    Environment = "dev"
  }
}