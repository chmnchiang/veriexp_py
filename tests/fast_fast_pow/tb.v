`timescale 1ns/100ps


module TB ();
reg clk;
reg [255:0] A;
reg [255:0] B;
reg [255:0] M;
reg start;
wire [255:0] result;
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
    A = 256'hbab4ced90e27661d82339709844497ee86760526d9766009083c2f39a55c6049;
    B = 256'h715637a09f055934ea3566b2c942a2db040ef70a64aab4d086e50291cef6e547;
    M = 256'hc485187e36c221d024345106cf3224212172df81d5be65306bedc648f00a3553;
    #1 start = 0;

    #1
    while (!done) begin
        #1;
    end
    $display(result);
    if (result != 256'h9c0d4b2181f8e1b369a00fb4a9f18d1799f3022625e1f63bf7d404ccd2e53237) begin
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
