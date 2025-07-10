module sumador4bits(
	input [7:0] a, 
	input [7:0] b, 
	output [7:0] sum,
	output Fcarry);
	
	wire [7:0] carry;
	
  Sumadorcompleto fa0(a[0], b[0], 1'b0, sum[0], carry[0]);
  Sumadorcompleto fa1(a[1], b[1], carry[0], sum[1], carry[1]);
  Sumadorcompleto fa2(a[2], b[2], carry[1], sum[2], carry[2]);
  Sumadorcompleto fa3(a[3], b[3], carry[2], sum[3], carry[3]);
  Sumadorcompleto fa4(a[4], b[4], carry[3], sum[4], carry[4]);
  Sumadorcompleto fa5(a[5], b[5], carry[4], sum[5], carry[5]);
  Sumadorcompleto fa6(a[6], b[6], carry[5], sum[6], carry[6]);
  Sumadorcompleto fa7(a[7], b[7], carry[6], sum[7], carry[7]);
  assign Fcarry=carry[6];
endmodule

module sumador4bits_tb;


  reg [7:0] a;
  reg [7:0] b;


  wire [7:0] sum;
  wire Fcarry;

  
  sumador4bits uut (
    .a(a),
    .b(b),
    .sum(sum),
	 .Fcarry(Fcarry)
  );

  initial begin

    a = 4'b00000000;
    b = 4'b00000000;

    #10;

    a = 4'b00010100; b = 4'b00100000;
    #10;
    a = 4'b00101010; b = 4'b00100100;
    #10;
    a = 4'b00101010; b = 4'b00010100;
    #10;
    a = 4'b00001010; b = 4'b00010111;
    #10;
    a = 4'b01101000; b = 4'b01001001;
    #10;
    a = 4'b00001011; b = 4'b11001010;
    #10;
    a = 4'b01110000; b = 4'b01010010;
    #10;
    a = 4'b01100101; b = 4'b00001100;
    #10;
    $finish;
  end
endmodule


