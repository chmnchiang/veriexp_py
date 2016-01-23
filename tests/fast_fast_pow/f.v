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
 wire gdone;
 wire [259:0] gres;
 reg _T1;
 wire [259:0] _T2;
 wire _T3;
 reg [259:0] _T4;
g _T5(
.clk(clk),
.start(_T0),
.done(gdone),
.reset(reset),
.result(gres),
.b(temp),
.m(_m),
.a(_a)
);
g _T6(
.clk(clk),
.start(_T1),
.done(_T3),
.reset(reset),
.result(_T2),
.b(_a),
.m(_m),
.a(_a)
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
_T1 <= 0;
_T4 <= 0;
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
state <= ((_b) & (1)) ? (19) : (23);
end
19: begin
_T0 <= 1;
state <= 21;
end
21: begin
_T0 <= 0;
state <= 23;
end
22: begin
state <= ((_b) & (1)) ? (29) : (28);
end
23: begin
_T1 <= 1;
state <= 24;
end
24: begin
_T1 <= 0;
state <= 25;
end
25: begin
state <= (_T3) ? (26) : (25);
end
26: begin
_T4 <= _T2;
state <= 27;
end
27: begin
_a <= _T4;
state <= 22;
end
28: begin
_b <= (_b) >> (1);
state <= 9;
end
29: begin
state <= (!(gdone)) ? (29) : (30);
end
30: begin
temp <= gres;
state <= 28;
end
endcase
end
end
endmodule

