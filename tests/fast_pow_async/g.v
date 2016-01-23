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
 reg [31:0] counter;
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
temp <= 0;
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
state <= ((temp) >= (_m)) ? (21) : (20);
end
10: begin
state <= ((_b) & (1)) ? (12) : (11);
end
11: begin
state <= ((temp) & (1)) ? (15) : (14);
end
12: begin
temp <= (temp) + (_a);
state <= 11;
end
14: begin
temp <= (temp) >> (1);
state <= 17;
end
15: begin
temp <= (temp) + (_m);
state <= 14;
end
17: begin
_b <= (_b) >> (1);
state <= 18;
end
18: begin
counter <= (counter) - (1);
state <= 6;
end
20: begin
result <= temp;
done <= 1;
state <= 0;
end
21: begin
temp <= (temp) - (_m);
state <= 20;
end
endcase
end
end
endmodule

