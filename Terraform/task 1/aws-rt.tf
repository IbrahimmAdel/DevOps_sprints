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


