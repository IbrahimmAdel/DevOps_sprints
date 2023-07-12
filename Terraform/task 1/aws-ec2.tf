data "aws_ami" "ubuntu" {
    most_recent = true
 
    filter {
        name   = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
    }
 
    filter {
        name   = "virtualization-type"
        values = ["hvm"]
    }
 
    filter {
        name   = "architecture"
        values = ["x86_64"]
    }
 
    owners = ["099720109477"]
}
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