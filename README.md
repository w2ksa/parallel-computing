# Parallel Computing

## Token Ring Printer Simulation

### Project Overview
This project simulates a Token Ring protocol using Python.  
The idea is to coordinate multiple processes that need to access a shared printer resource, ensuring that only one process prints at a time by using a token-based system.

### Objectives
- Simulate the concept of Token Passing between multiple processes.
- Manage access to a shared resource (printer) in a synchronized and conflict-free manner.
- Implement concurrency using Threads.
- Use Queues for simple message passing between processes.

### Implementation Details
- Each process is represented as a Python Thread.
- Each process can:
  - Request access to the printer.
  - Wait for the token.
  - Print documents (three times per process).
  - Pass the token to the next process.
- Communication between processes is handled through a Queue for each process.
- Random delays are introduced to simulate realistic timing for printing and requesting.

### How It Works
1. Three processes are created.
2. Process 0 initially holds the token.
3. Processes randomly decide when to request the printer.
4. If a process has the token and wants to print:
   - It prints one document.
5. After completing all three print jobs, it passes the token to the next process.
6. The simulation ends when all processes complete their printing tasks.

### Project Structure
- **Process class**:
  - Manages each individual process behavior.
  - Handles printer access, token receiving, and passing.

- **main() function**:
  - Initializes processes and threads.
  - Starts execution.
  - Waits for all threads to finish.

### Output
- All simulation outputs are written to `token_ring_output.txt` and then printed to the console at the end.

### How to Run
Make sure you have Python installed, then run:

```bash
python Problem\ 3\ Distributed\ Mutual\ Exclusion\ Algorithm.py
