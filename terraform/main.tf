terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

resource "aws_default_vpc" "default" {}

#configure provider
provider "aws" {
  region = "us-east-1"
}

#configure ec2 -> HTTP 80, 22, CIDR ["0.0.0.0/0"]
#security group -> 

resource "aws_security_group" "coen6313_project_sg" {
  name = "coen6313_project_sg"
  #vpc_id = "vpc-028538eed195469b3"
  #better way to do is below
  vpc_id = aws_default_vpc.default.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 9874
    to_port     = 9874
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1 #allow everything
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    name = "coen6313_project_sg"
  }
}

resource "aws_instance" "coen6313_project_server" {
  #ami                    = "ami-066784287e358dad1"
  ami                    = "ami-0866a3c8686eaeeba"
  key_name               = var.aws_key_pair_name
  instance_type          = var.aws_ami_Instance_type
  vpc_security_group_ids = [aws_security_group.coen6313_project_sg.id]
  subnet_id              = data.aws_subnets.default_subnets.ids[0]

#   connection {
#     type        = "ssh"
#     host        = self.public_ip
#     user        = "ubuntu"
#     private_key = file(var.aws_key_pair)
#   }

#   provisioner "remote-exec" {
#     inline = [
#       "sudo apt update",                                           
#       "sudo snap install docker",                                             
#     #   "echo Server at ${self.public_dns} | sudo tee /var/www/html/index.html" #copy index.html file
#     ]
#   }
}