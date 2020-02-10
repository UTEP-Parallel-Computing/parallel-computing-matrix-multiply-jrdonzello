Assignment 1 Part 2 Report: Implementing Parallel
The two main problems that occurred when working on this was where in the code to actually implement the parallel part and what elements need to be included in the parallel part. There are no bugs to my knowledge and everything should be working correctly.

This assignment took nearly 3 hours, half working on implementation and testing the program and the other half was for running the program to generate results.

Performance Stats: (Testing with size=1000)
1 thread : 0.72~0.79
2 threads : 0.35~0.40
4 threads : 0.193~0.22
8 threads : 0.10~0.12

By doubling the amount of threads, the amount of time is almost half of the previous time elapsed. This correlates with how I originally thought the program would react and logically/theoretically makes sense as well.

dumpCPUInfo.sh output:
model name	: Intel(R) Core(TM) i5-7360U CPU @ 2.30GHz
      1       9      54


Assignment 1 Report: Serial Matrix Multiplication

This Python script runs the standard way by calling the main file's name, 'python3 matrixMain.py'.
Once started the program will ask for either a custom value or to use the standard input.
You can enter your own pair of values with a space inbetween. E.g '9 10'

Very straight-forward programming assignment. Did not run into any problems.
I simply multiplied the value at the index by itself.
I was not sure if we were hard coding a specific number, multiplying two matrices together or if it even mattered.

This assignment took about an hour to complete.
