# parallel-computing
Token Ring Printer Simulation
Project Overview
This project simulates a Token Ring protocol using Python.
The idea is to coordinate multiple processes that need to access a shared printer resource, ensuring that only one process prints at a time by using a token-based system.

Objectives
Simulate the concept of Token Passing between multiple processes.

Manage access to a shared resource (printer) in a synchronized and conflict-free manner.

Implement concurrency using Threads.

Use Queues for simple message passing between processes.

Implementation Details
Each process is represented as a Python Thread.

Each process can:

Request access to the printer.

Wait for the token.

Print documents (three times per process).

Pass the token to the next process.

Communication between processes is handled through a Queue for each process.

Random delays are introduced to simulate realistic timing for printing and requesting.

How It Works
Three processes are created.

Process 0 initially holds the token.

Processes randomly decide when to request the printer.

If a process has the token and wants to print:

It prints one document.

After completing all three print jobs, it passes the token to the next process.

The simulation ends when all processes complete their printing tasks.

Project Structure
Process class:

Manages each individual process behavior.

Handles printer access, token receiving, and passing.

main() function:

Initializes processes and threads.

Starts execution.

Waits for all threads to finish.

All simulation outputs are written to token_ring_output.txt and then printed to the console at the end.

How to Run
Make sure you have Python installed. Then run:


python token_ring_simulation.py
After execution, you will find the output log in token_ring_output.txt.

Notes
The simulation involves random decision-making and random delays, so the exact order of events may vary with each execution.

The project uses only standard Python libraries (threading, queue, time, random, sys).

Concepts Demonstrated
Synchronized access to shared resources.

Multithreading and concurrency management.

Thread-safe communication using Queues.

Real-world inspired simulation of distributed systems.

