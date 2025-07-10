module Sumadorcompleto
	(input a, 
	input b, 
	input cin, 
	output sum, 
	output cout);
	
  wire ha1_sum, ha1_carry, ha2_sum, ha2_carry;
  mediosumador ha1(a, b, ha1_sum, ha1_carry);
  mediosumador ha2(ha1_sum, cin, ha2_sum, ha2_carry);
  assign sum = ha2_sum;
  assign cout = ha1_carry | ha2_carry;
endmodule

module Sumadorcompleto_tb;

  // Inputs
  reg a;
  reg b;
  reg cin;

  // Outputs
  wire sum;
  wire cout;


  Sumadorcompleto uut (
    .a(a),
    .b(b),
    .cin(cin),
    .sum(sum),
    .cout(cout)
  );

  initial begin

    a = 0;
    b = 0;
    cin = 0;

    #10;
    a = 0; b = 0; cin = 0;
    #10;
    a = 0; b = 0; cin = 1;
    #10;
    a = 0; b = 1; cin = 0;
    #10;
    a = 0; b = 1; cin = 1;
    #10;
    a = 1; b = 0; cin = 0;
    #10;
    a = 1; b = 0; cin = 1;
    #10;
    a = 1; b = 1; cin = 0;
    #10;
    a = 1; b = 1; cin = 1;
    #10;
    $finish;
  end
endmodule