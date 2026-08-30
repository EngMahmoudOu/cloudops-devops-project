output "ec2_public_ip" {
  description = "Public IP address of the CloudOps EC2 instance"
  value       = aws_instance.cloudops_server.public_ip
}

output "vpc_id" {
  description = "CloudOps VPC ID"
  value       = aws_vpc.cloudops_vpc.id
}

output "public_subnet_1_id" {
  description = "First public subnet ID"
  value       = aws_subnet.public_1.id
}
