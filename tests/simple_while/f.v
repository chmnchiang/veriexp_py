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
 reg [31:0] t;
 reg [31:0] res;
always @(posedge clk) begin
if (reset) state <= 0; else begin
case(state)
0: begin
state <= (start) ? (1) : (0);
end
1: begin
_a <= a;
_b <= b;
state <= 4;
done <= 0;
end
4: begin
t <= _b;
state <= 5;
end
5: begin
res <= 0;
state <= 6;
end
6: begin
state <= ((t) != (0)) ? (8) : (7);
end
7: begin
result <= res;
done <= 1;
state <= 0;
end
8: begin
res <= (res) + (_a);
state <= 9;
end
9: begin
t <= (t) - (1);
state <= 6;
end
endcase
end
end
endmodule

