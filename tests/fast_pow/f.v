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
 reg [31:0] temp;
always @(posedge clk) begin
if (reset) begin
state <= 0;
result <= 0;
done <= 0;
_a <= 0;
_b <= 0;
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
state <= ((_b) & (1)) ? (8) : (7);
end
7: begin
_b <= (_b) >> (1);
state <= 10;
end
8: begin
temp <= (temp) * (_a);
state <= 7;
end
10: begin
_a <= (_a) * (_a);
state <= 4;
end
endcase
end
end
endmodule

