module ALU (
  input wire clk,
  input wire reset,
  input wire start,
  input wire [7:0] operand1,
  input wire [7:0] operand2,
  input wire [2:0] opcode,
  output reg [15:0] result,
  output wire done
);

  reg [7:0] reg_operand1;
  reg [7:0] reg_operand2;
  reg [2:0] reg_opcode;
  reg [15:0] reg_result;
  reg reg_done;

  always @(posedge clk) begin
    if (reset) begin
      reg_done <= 0;
      reg_result <= 0;
    end else begin
      if (start) begin
        reg_done <= 0;
        reg_operand1 <= operand1;
        reg_operand2 <= operand2;
        reg_opcode <= opcode;
        case (reg_opcode)
          3'b000: reg_result <= reg_operand1 + reg_operand2; // Suma
          3'b001: reg_result <= reg_operand1 - reg_operand2; // Resta
          3'b010: reg_result <= reg_operand1 * reg_operand2; // Multiplicación
          3'b011: reg_result <= reg_operand1 & reg_operand2; // AND lógico
          3'b100: reg_result <= reg_operand1 | reg_operand2; // OR lógico
          3'b101: reg_result <= reg_operand1 ^ reg_operand2; // XOR lógico
          default: reg_result <= 16'd0; // NOP (no operation)
        endcase
        reg_done <= 1;
      end else begin
        reg_done <= 0;
      end
    end
  end

  assign done = reg_done;

  always @(reg_result) begin
    result <= reg_result;
  end

endmodule

module ALU_tb;
  reg clk;
  reg reset;
  reg start;
  reg [7:0] operand1;
  reg [7:0] operand2;
  reg [2:0] opcode;
  wire [15:0] result;
  wire done;

  ALU dut (
    .clk(clk),
    .reset(reset),
    .start(start),
    .operand1(operand1),
    .operand2(operand2),
    .opcode(opcode),
    .result(result),
    .done(done)
  );

  initial begin
    clk = 0;
    reset = 1;
    start = 0;
    operand1 = 0;
    operand2 = 0;
    opcode = 0;
    #10 reset = 0; // Desactivar reset

    // Prueba de suma
    operand1 = 10;
    operand2 = 5;
    opcode = 0;
    start = 1;
    #20 start = 0;
    #10 $display("Suma: Resultado = %d, Esperado = 15, %s", result, (result == 15) ? "PASSED" : "FAILED");

    // Prueba de resta
    operand1 = 10;
    operand2 = 5;
    opcode = 1;
    start = 1;
    #20 start = 0;
    #10 $display("Resta: Resultado = %d, Esperado = 5, %s", result, (result == 5) ? "PASSED" : "FAILED");

    // Prueba de multiplicación
    operand1 = 10;
    operand2 = 5;
    opcode = 2;
    start = 1;
    #20 start = 0;
    #10 $display("Multiplicación: Resultado = %d, Esperado = 50, %s", result, (result == 50) ? "PASSED" : "FAILED");

    // Prueba de AND lógico
    operand1 = 10;
    operand2 = 5;
    opcode = 3;
    start = 1;
    #20 start = 0;
    #10 $display("AND lógico: Resultado = %d, Esperado = 0, %s", result, (result == 0) ? "PASSED" : "FAILED");

    // Prueba de OR lógico
    operand1 = 10;
    operand2 = 5;
    opcode = 4;
    start = 1;
    #20 start = 0;
    #10 $display("OR lógico: Resultado = %d, Esperado = 15, %s", result, (result == 15) ? "PASSED" : "FAILED");

    // Prueba de XOR lógico
    operand1 = 10;
    operand2 = 5;
    opcode = 5;
    start = 1;
    #20 start = 0;
    #10 $display("XOR lógico: Resultado = %d, Esperado = 15, %s", result, (result == 15) ? "PASSED" : "FAILED");

    // Prueba de NOP
    operand1 = 0;
    operand2 = 0;
    opcode = 7;
    start = 1;
    #20 start = 0;
    #10 $display("NOP: Resultado = %d, Esperado = 0, %s", result, (result == 0) ? "PASSED" : "FAILED");

    $finish;
  end

  always #5 clk = ~clk;

endmodule



