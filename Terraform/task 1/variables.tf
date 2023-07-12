# EC2 Variables
variable "instance_name" {
        default = "sprints_ec2"
}
variable "instance_type" {
        default = "t2.micro"
}

# VPC Variables
variable "vpc_cidr_block" {
        default = "10.0.0.0/16"
}
variable "vpc_name" {
        default = "Sprints_VPC"
}

# subnet Variables
variable "subnet_cidr_block" {
        default = "10.0.0.0/24"
}
variable "AZ" {
        default = "us-east-1a"
}
variable "subnet_name" {
        default = "sprints_pub_Subnet"
}

# internet gateway Variables
variable "ig_name" {
        default = "sprints-ig"
}

# route table Variables
variable "rt_name" {
        default = "Public Route Table"
}
variable "cidr_block" {
        default = "0.0.0.0/0"
}
