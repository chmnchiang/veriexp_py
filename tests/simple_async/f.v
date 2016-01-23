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
 reg _T0;
 wire d1;
 wire [31:0] r1;
 reg _T1;
 wire d2;
 wire [31:0] r2;
 reg _T2;
 wire d3;
 wire [31:0] r3;
 reg [31:0] res;
g _T3(
.clk(clk),
.reset(reset),
.a(_a),
.b(_a),
.start(_T0),
.result(r1),
.done(d1)
);
g _T4(
.clk(clk),
.reset(reset),
.a(_a),
.b(_b),
.start(_T1),
.result(r2),
.done(d2)
);
g _T5(
.clk(clk),
.reset(reset),
.a(_b),
.b(_b),
.start(_T2),
.result(r3),
.done(d3)
);
always @(posedge clk) begin
if (reset) begin
state <= 0;
result <= 0;
done <= 0;
_a <= 0;
_b <= 0;
_T0 <= 0;
_T1 <= 0;
_T2 <= 0;
res <= 0;
end else begin
case(state)
0: begin
state <= (start) ? (1) : (0);
done <= (start) ? (0) : (1);
end
1: begin
_a <= a;
_b <= b;
state <= 2;
end
2: begin
_T0 <= 1;
state <= 4;
end
3: begin
_T1 <= 1;
state <= 6;
end
4: begin
_T0 <= 0;
state <= 3;
end
5: begin
_T2 <= 1;
state <= 8;
end
6: begin
_T1 <= 0;
state <= 5;
end
7: begin
state <= (!(((d1) && (d2)) && (d3))) ? (7) : (12);
end
8: begin
_T2 <= 0;
state <= 7;
end
11: begin
result <= res;
done <= 1;
state <= 0;
end
12: begin
res <= ((r1) + ((2) * (r2))) + (r3);
state <= 11;
end
endcase
end
end
endmodule

