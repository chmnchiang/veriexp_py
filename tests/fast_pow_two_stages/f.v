module f(clk, reset, start, result, done, a, b, m);
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
input wire [31:0] m;
 reg [31:0] _m;
 reg [31:0] temp;
 reg _T0;
 wire [31:0] _T1;
 wire _T2;
 reg [31:0] _T3;
 reg _T4;
 wire [31:0] _T5;
 wire _T6;
 reg [31:0] _T7;
g _T8(
.done(_T2),
.b(temp),
.a(_a),
.start(_T0),
.clk(clk),
.result(_T1),
.reset(reset),
.m(_m)
);
g _T9(
.done(_T6),
.b(_a),
.a(_a),
.start(_T4),
.clk(clk),
.result(_T5),
.reset(reset),
.m(_m)
);
always @(posedge clk) begin
if (reset) begin
state <= 0;
result <= 0;
done <= 0;
_a <= 0;
_b <= 0;
_m <= 0;
temp <= 0;
_T0 <= 0;
_T3 <= 0;
_T4 <= 0;
_T7 <= 0;
end else begin
case(state)
0: begin
state <= (start) ? (1) : (0);
done <= (start) ? (0) : (1);
end
1: begin
_a <= a;
_b <= b;
_m <= m;
state <= 3;
end
3: begin
temp <= 1;
state <= 4;
end
4: begin
state <= (_b) ? (6) : (5);
end
5: begin
result <= temp;
done <= 1;
state <= 0;
end
6: begin
state <= ((_b) & (1)) ? (10) : (7);
end
7: begin
_b <= (_b) >> (1);
state <= 17;
end
10: begin
_T0 <= 1;
state <= 11;
end
11: begin
_T0 <= 0;
state <= 12;
end
12: begin
state <= (_T2) ? (13) : (12);
end
13: begin
_T3 <= _T1;
state <= 14;
end
14: begin
temp <= _T3;
state <= 7;
end
17: begin
_T4 <= 1;
state <= 18;
end
18: begin
_T4 <= 0;
state <= 19;
end
19: begin
state <= (_T6) ? (20) : (19);
end
20: begin
_T7 <= _T5;
state <= 21;
end
21: begin
_a <= _T7;
state <= 4;
end
endcase
end
end
endmodule

