output "coen6313_project_sg_details" {
  value = aws_security_group.coen6313_project_sg
}

output "coen6313_project_public_dns" {
  value = aws_instance.coen6313_project_server.public_dns
}