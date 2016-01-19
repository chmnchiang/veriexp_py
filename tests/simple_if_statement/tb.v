`timescale 1ns/100ps


module TB ();
reg clk;
reg [31:0] A;
reg [31:0] B;
reg start;
wire [31:0] result;
wire done;
reg reset;

initial begin
    $dumpfile("tb.vcd");
    $dumpvars(0, TB);
end

f ff(.clk(clk), .reset(reset), .a(A), .b(B), .start(start), .result(result), .done(done));

always  begin
    #(0.5) clk = ~clk;
end

initial begin
    clk = 0;
    start = 0;
    reset = 0;
    #1 reset = 1;
    #1 reset = 0;
    
    #3;
    start = 1;
    A = 1;
    B = 2;
    #1 start = 0;

    #1
    while (!done) begin
        #1;
    end
    $display(result);
    if (result != 2) begin
        $display("error");
        $finish;
    end

    #3;
    start = 1;
    A = 7;
    B = 4;
    #1 start = 0;

    #1
    while (!done) begin
        #1;
    end
    $display(result);
    if (result != 7) begin
        $display("error");
        $finish;
    end

    $finish;
end
endmodule
