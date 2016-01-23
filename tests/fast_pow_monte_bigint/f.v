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
 reg [31:0] counter;
 reg _T0;
 wire [259:0] _T1;
 wire _T2;
 reg [259:0] _T3;
 reg _T4;
 wire [259:0] _T5;
 wire _T6;
 reg [259:0] _T7;
g _T8(
.start(_T0),
.done(_T2),
.reset(reset),
.m(_m),
.result(_T1),
.clk(clk),
.a(_a),
.b(temp)
);
g _T9(
.start(_T4),
.done(_T6),
.reset(reset),
.m(_m),
.result(_T5),
.clk(clk),
.a(_a),
.b(_a)
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
counter <= 0;
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
4: begin
temp <= 1;
state <= 7;
end
6: begin
state <= (counter) ? (10) : (9);
end
7: begin
counter <= 256;
state <= 6;
end
9: begin
state <= (_b) ? (17) : (16);
end
10: begin
_a <= (_a) << (1);
state <= 11;
end
11: begin
state <= ((_a) >= (_m)) ? (13) : (12);
end
12: begin
counter <= (counter) - (1);
state <= 6;
end
13: begin
_a <= (_a) - (_m);
state <= 12;
end
16: begin
result <= temp;
done <= 1;
state <= 0;
end
17: begin
state <= ((_b) & (1)) ? (21) : (18);
end
18: begin
_b <= (_b) >> (1);
state <= 28;
end
21: begin
_T0 <= 1;
state <= 22;
end
22: begin
_T0 <= 0;
state <= 23;
end
23: begin
state <= (_T2) ? (24) : (23);
end
24: begin
_T3 <= _T1;
state <= 25;
end
25: begin
temp <= _T3;
state <= 18;
end
28: begin
_T4 <= 1;
state <= 29;
end
29: begin
_T4 <= 0;
state <= 30;
end
30: begin
state <= (_T6) ? (31) : (30);
end
31: begin
_T7 <= _T5;
state <= 32;
end
32: begin
_a <= _T7;
state <= 9;
end
endcase
end
end
endmodule

