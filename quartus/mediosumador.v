module mediosumador(
	input a, 
	input b, 
	output sum, 
	output carry);
	
  assign sum = a ^ b;
  assign carry = a & b;
  
endmodule

module mediosumador_tb;
  reg a;
  reg b;
  wire sum;
  wire carry;
  mediosumador uut (
    .a(a),
    .b(b),
    .sum(sum),
    .carry(carry)
  );

  initial begin
    a = 0;
    b = 0;
    #10;
    a = 0; b = 0;
    #10;
    a = 0; b = 1;
    #10;
    a = 1; b = 0;
    #10;
    a = 1; b = 1;
    #10;
    $finish;
  end
endmodule