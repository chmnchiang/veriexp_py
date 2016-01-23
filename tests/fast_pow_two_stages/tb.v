`timescale 1ns/100ps


module TB ();
reg clk;
reg [31:0] A;
reg [31:0] B;
reg [31:0] M;
reg start;
wire [31:0] result;
wire done;
reg reset;

initial begin
    $dumpfile("tb.vcd");
    $dumpvars(0, TB);
end

f ff(.clk(clk), .reset(reset), .a(A), .b(B), .m(M), .start(start), .result(result), .done(done));

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
    M = 5;
    #1 start = 0;

    #1
    while (!done) begin
        #1;
    end
    $display(result);
    if (result != 1) begin
        $display("error");
        $finish;
    end

    #3;
    start = 1;
    A = 7;
    B = 5;
    M = 13;
    #1 start = 0;

    #1
    while (!done) begin
        #1;
    end
    $display(result);
    if (result != 11) begin
        $display("error");
        $finish;
    end

    #3;
    start = 1;
    A = 3;
    B = 19;
    M = 103;
    #1 start = 0;

    #1
    while (!done) begin
        #1;
    end
    $display(result);
    if (result != 94) begin
        $display("error");
        $finish;
    end

    #3;
    start = 1;
    A = 9081235;
    B = 3728103;
    M = 98234125;
    #1 start = 0;

    #1
    while (!done) begin
        #1;
    end
    $display(result);
    if (result != 23831250) begin
        $display("error");
        $finish;
    end

    $finish;
end
endmodule
