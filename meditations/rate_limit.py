
"""
// Perform rate limiting logic for provided customer ID. Return true if the
// request is allowed, and false if it is not.
boolean rateLimit(int customerId)

“Each customer can make X requests per Y seconds”

"""
from collections import deque

import time

class RateLimiter:
    def __init__(self, allowance, time_frame):
        self.capacity = allowance
        self.time_frame = time_frame
        self.user_queues = {}   #  {"customer 1": (deque: [], remaining)}

    # time: amortized O(1) over number of requests coming in
    # space: O(num_customers * capacity)
    def rateLimit(self, customer_id, debug_time=None):
        # if customer_id don't exist create a queue
        if customer_id not in self.user_queues:
            self.user_queues[customer_id] = deque([])
        
        queue, remaining = self.user_queues[customer_id]
        
        current_time = time.time()
        # print(current_time)
        # print(customer_id)
        while queue and queue[0] < current_time - self.time_frame:
            prev_time, prev_count = queue.popleft()
            remaining -= prev_count
            
        if len(queue) < self.capacity:
            queue.append(current_time, remaining + 1)
            return True
        return False
        

def tests():
    rt = RateLimiter(3, 1)
        
    print(rt.rateLimit("can"))
    print(rt.rateLimit("can"))
    print(rt.rateLimit("can"))
    print(rt.rateLimit("can"))
    print(rt.rateLimit("can"))
    time.sleep(1)
    print(rt.rateLimit("can"))
    print(rt.rateLimit("can"))
    print(rt.rateLimit("can"))
    print(rt.rateLimit("can"))
    print()
    # print(rt.rateLimit("karnesh"))
    # print(rt.rateLimit("karnesh"))
    # print(rt.rateLimit("karnesh"))
    # print(rt.rateLimit("karnesh"))
    # print(rt.rateLimit("karnesh"))
    # print(rt.rateLimit("karnesh"))
    # print(rt.rateLimit("karnesh"))
    # print(rt.rateLimit("karnesh"))
    # print(rt.rateLimit("karnesh"))
    # print(rt.rateLimit("karnesh"))
    
    time.sleep(0.1)
        
tests()



