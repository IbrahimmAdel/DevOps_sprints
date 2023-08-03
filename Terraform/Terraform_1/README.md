# Terraform TASK 1

## Network :
```
resource "aws_vpc" "vpc" {
 cidr_block = "${var.vpc_cidr_block}"
 
 tags = {
   Name = "${var.vpc_name}"
 }
}
```
```
resource "aws_subnet" "pub_subnet" {
    vpc_id = aws_vpc.vpc.id
    cidr_block = "${var.subnet_cidr_block}"
    availability_zone = "${var.AZ}"
    tags = {
        Name = "${var.subnet_name}"
    }
    }
```
```
resource "aws_internet_gateway" "gw" {
 vpc_id = aws_vpc.vpc.id
 tags = {
   Name = "${var.ig_name}"
 }
}
```
```
resource "aws_default_route_table" "public_rt" {
  default_route_table_id = aws_vpc.vpc.default_route_table_id

  route {
    cidr_block = "${var.cidr_block}"
    gateway_id = aws_internet_gateway.gw.id
  }
  tags = {
    Name = "${var.rt_name}"
  }
}
resource "aws_route_table_association" "sprints_rta" {
  subnet_id      = aws_subnet.pub_subnet.id
  route_table_id = aws_default_route_table.public_rt.id
}
```
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Terraform/Terraform_1/screenshots/Screenshot%20from%202023-07-05%2012-56-51.png)
## Instances :
```
resource "aws_instance" "ec2_instance" {
    instance_type = "${var.instance_type}"
    ami = data.aws_ami.ubuntu.id
    tags = {
        Name = "sprints-ec2"
        Description = "An Nginx WebServer on Ubuntu"
    }
    subnet_id  =  aws_subnet.pub_subnet.id
    security_groups = [aws_security_group.web_sg.id]
    availability_zone = "${var.AZ}"
    associate_public_ip_address = true
    user_data = "${file("script.sh")}"
} 
```
script to install apache
```
#!/bin/bash
sudo apt-get update
sudo apt-get install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2
```
```
resource "aws_security_group" "web_sg" {
  name   = "sprints-sg"
  vpc_id = aws_vpc.vpc.id

  ingress {
            from_port   = 443
            to_port     = 443
            protocol    = "tcp"
            cidr_blocks = ["0.0.0.0/0"]
          }
 ingress {
            from_port   = 22
            to_port     = 22
            protocol    = "tcp"
            cidr_blocks = ["0.0.0.0/0"]

          }
  ingress {
            from_port   = 80
            to_port     = 80
            protocol    = "tcp"
            cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
            from_port   = 0
            to_port     = 0
            protocol    = -1
            cidr_blocks = ["0.0.0.0/0"]
        }
  tags = {
    Name = "Sprints-SG"
  }
}
```
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Terraform/Terraform_1/screenshots/Screenshot%20from%202023-07-05%2012-58-14.png)
## apache page :
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Terraform/Terraform_1/screenshots/Screenshot%20from%202023-07-05%2012-49-44.png)
