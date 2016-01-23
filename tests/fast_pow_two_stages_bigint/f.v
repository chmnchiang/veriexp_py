module f(clk, reset, start, result, done, a, b, m);
 reg [31:0] state;
input wire clk;
input wire reset;
input wire start;
output reg [259:0] result;
output reg done;
input wire [259:0] a;
 reg [259:0] _a;
input wire [259:0] b;
 reg [259:0] _b;
input wire [259:0] m;
 reg [259:0] _m;
 reg [259:0] temp;
 reg _T0;
 wire [259:0] _T1;
 wire _T2;
 reg [259:0] _T3;
 reg _T4;
 wire [259:0] _T5;
 wire _T6;
 reg [259:0] _T7;
g _T8(
.done(_T2),
.result(_T1),
.clk(clk),
.reset(reset),
.b(temp),
.start(_T0),
.a(_a),
.m(_m)
);
g _T9(
.done(_T6),
.result(_T5),
.clk(clk),
.reset(reset),
.b(_a),
.start(_T4),
.a(_a),
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
state <= 4;
end
3: begin
state <= (_b) ? (7) : (6);
end
4: begin
temp <= 1;
state <= 3;
end
6: begin
result <= temp;
done <= 1;
state <= 0;
end
7: begin
state <= ((_b) & (1)) ? (11) : (8);
end
8: begin
_b <= (_b) >> (1);
state <= 18;
end
11: begin
_T0 <= 1;
state <= 12;
end
12: begin
_T0 <= 0;
state <= 13;
end
13: begin
state <= (_T2) ? (14) : (13);
end
14: begin
_T3 <= _T1;
state <= 15;
end
15: begin
temp <= _T3;
state <= 8;
end
18: begin
_T4 <= 1;
state <= 19;
end
19: begin
_T4 <= 0;
state <= 20;
end
20: begin
state <= (_T6) ? (21) : (20);
end
21: begin
_T7 <= _T5;
state <= 22;
end
22: begin
_a <= _T7;
state <= 3;
end
endcase
end
end
endmodule

