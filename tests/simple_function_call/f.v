module f(clk, reset, start, result, done, a, b);
 reg [31:0] state;
input wire clk;
input wire reset;
input wire start;
output reg [31:0] result;
output reg done;
input wire [31:0] a;
 reg [31:0] _a;
input wire [31:0] b;
 reg [31:0] _b;
 reg [31:0] c;
 reg _T0;
 wire [31:0] _T1;
 wire _T2;
 reg [31:0] _T3;
g _T4(
.clk(clk),
.reset(reset),
.result(_T1),
.start(_T0),
.done(_T2),
.b(_b),
.a(_a)
);
always @(posedge clk) begin
if (reset) begin
state <= 0;
result <= 0;
done <= 0;
_a <= 0;
_b <= 0;
c <= 0;
_T0 <= 0;
_T3 <= 0;
end else begin
case(state)
0: begin
state <= (start) ? (1) : (0);
done <= (start) ? (0) : (1);
end
1: begin
_a <= a;
_b <= b;
state <= 5;
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
_T0 <= 0;
state <= 7;
end
7: begin
state <= (_T2) ? (8) : (7);
end
8: begin
_T3 <= _T1;
state <= 9;
end
9: begin
c <= _T3;
state <= 4;
end
endcase
end
end
endmodule

