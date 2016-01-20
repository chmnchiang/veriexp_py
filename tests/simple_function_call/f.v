module f(clk, reset, start, a, b, result, done);
 reg [31:0] state;
input wire clk;
input wire reset;
input wire start;
input wire [31:0] a;
 reg [31:0] _a;
input wire [31:0] b;
 reg [31:0] _b;
output reg [31:0] result;
output reg done;
 reg [31:0] c;
 reg _T0;
 wire [31:0] _T1;
 wire _T2;
 reg [31:0] _T3;
g _T4(
.start(_T0),
.clk(clk),
.b(_b),
.reset(reset),
.done(_T2),
.result(_T1),
.a(_a)
);
always @(posedge clk) begin
if (reset) begin
state <= 0;
_a <= 0;
_b <= 0;
result <= 0;
done <= 0;
c <= 0;
_T0 <= 0;
_T3 <= 0;
end else begin
case(state)
0: begin
state <= (start) ? (1) : (0);
end
1: begin
_a <= a;
_b <= b;
state <= 5;
done <= 0;
end
4: begin
result <= c;
done <= 1;
state <= 0;
end
5: begin
_T0 <= 1;
state <= 6;
end
6: begin
state <= (_T2) ? (7) : (6);
end
7: begin
_T3 <= _T1;
state <= 8;
end
8: begin
c <= _T1;
state <= 4;
end
endcase
end
end
endmodule

