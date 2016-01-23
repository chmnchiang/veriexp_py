module g(clk, reset, start, result, done, a, b, m);
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
always @(posedge clk) begin
if (reset) begin
state <= 0;
result <= 0;
done <= 0;
_a <= 0;
_b <= 0;
_m <= 0;
temp <= 0;
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
temp <= 0;
state <= 3;
end
6: begin
result <= temp;
done <= 1;
state <= 0;
end
7: begin
state <= ((_b) & (1)) ? (9) : (8);
end
8: begin
_b <= (_b) >> (1);
state <= 14;
end
9: begin
temp <= (temp) + (_a);
state <= 10;
end
10: begin
state <= ((temp) >= (_m)) ? (12) : (8);
end
12: begin
temp <= (temp) - (_m);
state <= 8;
end
14: begin
_a <= (_a) << (1);
state <= 15;
end
15: begin
state <= ((_a) >= (_m)) ? (17) : (3);
end
17: begin
_a <= (_a) - (_m);
state <= 3;
end
endcase
end
end
endmodule

