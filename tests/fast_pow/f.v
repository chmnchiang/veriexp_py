module f(clk, reset, start, a, b, result, done);
 reg [31:0] state;
input wire clk;
input wire reset;
input wire start;
input wire [31:0] a;
 reg [31:0] _a;
input wire [31:0] b;
 reg [31:0] _b;
output reg [31:0] result;
output reg done;
 reg [31:0] temp;
always @(posedge clk) begin
if (reset) state <= 0; else begin
case(state)
0: begin
state <= (start) ? (1) : (0);
end
1: begin
_a <= a;
_b <= b;
state <= 3;
done <= 0;
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

