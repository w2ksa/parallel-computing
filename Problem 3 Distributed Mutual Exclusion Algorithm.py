#Problem 3: Distributed Mutual Exclusion Algorithm
import threading
import time
import random
from queue import Queue

class Process(threading.Thread):
    def __init__(self, process_id, total_processes, token_queue):
        super().__init__()
        self.process_id = process_id
        self.total_processes = total_processes
        self.token_queue = token_queue
        self.has_token = False
        self.want_to_print = False
        self.print_count = 0
        self.max_prints = 3 



    def run(self):
        while self.print_count < self.max_prints:
            if self.has_token:
                if self.want_to_print:
                    self.print_document()
                    self.want_to_print = False
                self.pass_token()
            else:
                time.sleep(0.1)  

    def request_printer(self):
        print(f"Process {self.process_id} is requesting access to the printer.")
        self.want_to_print = True

    def print_document(self):
        print(f"Process {self.process_id} is printing document #{self.print_count + 1}")
        time.sleep(random.uniform(0.5, 1.0))  
        self.print_count += 1
        print(f"Process {self.process_id} finished printing.")

    def pass_token(self):
        next_process = (self.process_id + 1) % self.total_processes
        self.token_queue[next_process].put("TOKEN")
        self.has_token = False
        print(f"Process {self.process_id} passed the token to Process {next_process}.")

def token_listener(process: Process):
    while process.print_count < process.max_prints:
        try:
            message = process.token_queue[process.process_id].get(timeout=1)
            if message == "TOKEN":
                process.has_token = True
        except:
            continue

def main():
    total_processes = 3
    token_queue = [Queue() for _ in range(total_processes)]
    processes = [Process(i, total_processes, token_queue) for i in range(total_processes)]



    listeners = [threading.Thread(target=token_listener, args=(p,)) for p in processes]
    for listener in listeners:
        listener.start()

    for p in processes:
        p.start()

    processes[0].has_token = True


    while any(p.is_alive() for p in processes):
        random.choice(processes).request_printer()
        time.sleep(random.uniform(0.5, 2.0))

    for p in processes:
        p.join()
    for listener in listeners:
        listener.join()


    print("All processes completed printing.")



if __name__ == "__main__":
    main()
