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
always @(posedge clk) begin
if (reset) begin
state <= 0;
_a <= 0;
_b <= 0;
result <= 0;
done <= 0;
end else begin
case(state)
0: begin
state <= (start) ? (1) : (0);
end
1: begin
_a <= a;
_b <= b;
state <= 2;
done <= 0;
end
2: begin
result <= (_a) + (_b);
done <= 1;
state <= 0;
end
endcase
end
end
endmodule

