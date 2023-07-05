resource "aws_subnet" "pub_subnet" {
    vpc_id = aws_vpc.vpc.id
    cidr_block = "${var.subnet_cidr_block}"
    availability_zone = "${var.AZ}"
    tags = {
        Name = "${var.subnet_name}"
    }
    }
