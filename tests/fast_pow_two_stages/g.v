module g(clk, reset, start, result, done, a, b, m);
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
state <= 3;
end
3: begin
temp <= 0;
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
state <= ((_b) & (1)) ? (8) : (7);
end
7: begin
_b <= (_b) >> (1);
state <= 13;
end
8: begin
temp <= (temp) + (_a);
state <= 9;
end
9: begin
state <= ((temp) >= (_m)) ? (11) : (7);
end
11: begin
temp <= (temp) - (_m);
state <= 7;
end
13: begin
_a <= (_a) + (_a);
state <= 14;
end
14: begin
state <= ((_a) >= (_m)) ? (16) : (4);
end
16: begin
_a <= (_a) - (_m);
state <= 4;
end
endcase
end
end
endmodule

