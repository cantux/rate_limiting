from collections import deque
import threading
import time

class RateLimiter(object):
    def __init__(self, user_limit_dict={}):
        self.u_q = {user_id: 
                    (limit_cond[0], limit_cond[1], deque(), threading.Lock()) 
                        for (user_id, limit_cond) in user_limit_dict.items()
                } 

    def is_allowed(self, user_id, *args):
        user_data = self.u_q[user_id]
        limit_count = user_data[0]
        limit_time_frame = user_data[1]
        req_queue = user_data[2]
        req_queue_lock = user_data[3]
        with req_queue_lock:
            current_time = args[0] if args else time.time()
            RateLimiter.evict(req_queue, limit_time_frame, current_time)
            if len(req_queue) > limit_count:
                raise RateLimiter.ApiRateLimitReachedException(
                     "user: {0} exceeded limit: {1}".format(user_id, limit_count))
            else:
                req_queue.append(current_time)

    @staticmethod
    def evict(req_queue, time_window_seconds, current_time):
        while req_queue and req_queue[0] < (current_time - time_window_seconds):
            req_queue.popleft()

    class ApiRateLimitReachedException(Exception):
        pass


def test():
    ul_dict = {"can": [5, 10], "murat": [5, 10]}
    rl = RateLimiter(ul_dict)
    def test_run(**args):
        try:
            rl.is_allowed(args["u_id"], args["time"])
        except RateLimiter.ApiRateLimitReachedException as e:
            print("thread {0} raised ex".format(args["time"]), e)
            
    # can makes 1 request every second. since time_window is set to 10 seconds. 
    # He will not be allowed 5 requests but be allowed the last one.
    can_threads = [threading.Thread(target=test_run, kwargs={"u_id": "can", "time": i}) for i in range(11)]
    
    # murat makes 1 request every 2 second. Since his limit is 5 and time window is 10 seconds all of his requests will be allowed.
    murat_threads = [threading.Thread(target=test_run, kwargs={"u_id": "murat", "time": i*2}) for i in range(11)]
    
    for i in range(11):
        can_threads[i].start()
        murat_threads[i].start()


if __name__ == "__main__":
    test()

    
