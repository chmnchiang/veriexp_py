A C-like to Verilog compiler

# How to use
./veriexp input.ver > output.v

# Syntax
## Variable declaration
```
int a;
```
## Assignment
```
a = b + c * 2;
```
## If else
```
if (a < b) {
} else if (a > b) {
} else {
}
```
## While
```
while (a) { ... }
```
## Function Call
```
func_name( args ) -> return_type
a = (f(addr=b, value=c) -> int) * d;
```
## Async function call
async fdone, fres = f(addr=b, value=c) -> d;
await fdone;
