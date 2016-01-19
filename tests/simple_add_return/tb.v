`timescale 1ns/100ps


module TB ();
reg clk;
reg [31:0] A;
reg [31:0] B;
reg start;
wire [31:0] result;
reg reset;

initial begin
    $dumpfile("tb.vcd");
    $dumpvars(0, TB);
end

f ff(.clk(clk), .reset(reset), .a(A), .b(B), .start(start), .result(result));

always  begin
    #(1) clk = ~clk;
end

initial begin
    clk = 0;
    A = 10;
    B = 20;
    start = 0;
    reset = 0;
    #1 reset = 1;
    #1 reset = 0;
    
    #3 start = 1;
    #1 start = 0;

    #4;
    $display(result);
    if (result != 30) begin
        $display("error");
    end
    $finish;
end
endmodule
