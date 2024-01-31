from collections import deque
import threading
import time

class RateLimiter(object):
    def __init__(self, ul_dict, time_window_seconds):
        """
        @desc constr
        @param ul_dict hashmap of unique user ids to their limits
        """
        # create a dictionary of users, their max limits, request queue and a lock for that request queue
        self.u_q = {u: (l, deque(), threading.Lock()) for (u, l) in ul_dict.items()} 
        self.time_window_seconds = time_window_seconds
        self.lock = threading.Lock() # make it a thread safe service
    
    def addUser(user_id, user_limit):
        with self.lock:
            self.u_q.update({user_id: (user_limit, 0, deque(), threading.Lock())})

    def removeUser(self, user_id):
        with self.lock:
            del self.u_q[user_id]

    def isAllowed(self, user_id, *args):
        """
        @desc check if user is allowed to make a request.
                evict on every request
        @param user_id
        @param args list of test arguments. currently used for specifying the arrival of a request
        """
        user_data = self.u_q[user_id]
        limit = user_data[0]
        req_queue = user_data[1]
        req_queue_lock = user_data[2]

        with req_queue_lock:
            current_time = args[0] if args else time.time()
            RateLimiter.evict(req_queue, self.time_window_seconds, current_time)

            if len(req_queue) >= limit:
                raise RateLimiter.ApiRateLimitReachedException("user: {user_id}, exceeded limit: {limit}".format(user_id=user_id, limit=limit))
            else:
                req_queue.append(current_time)
    
    @staticmethod
    def evict(req_queue, time_window_seconds, current_time):
        """
        @desc evict request entries from the queue if they are older than current_time - time_window
                test use first list argument
        """
        if req_queue: 
            # if the first entry in the queue is smaller then 
            if req_queue[0] <= current_time - time_window_seconds:
                while req_queue.popleft() <= current_time - time_window_seconds:
                    continue

    class ApiRateLimitReachedException(Exception):
        pass

def test():
    ul_dict = {"can": 5, "murat": 5}
    rl = RateLimiter(ul_dict, 10)
    def test_run(**args):
        try:
            rl.isAllowed(args["u_id"], args["time"])
        except RateLimiter.ApiRateLimitReachedException, e:
            print "thread {0} raised ex".format(args["time"])
            
    # can makes 1 request every second. since time_window is set to 10 seconds. 
    # He will not be allowed 5 requests but be allowed the last one.
    can_threads = [threading.Thread(target=test_run, kwargs={"u_id": "can", "time": i}) for i in range(11)]
    
    # murat makes 1 request every 2 second. Since his limit is 6 and time window is 10 seconds all of his requests will be allowed.
    murat_threads = [threading.Thread(target=test_run, kwargs={"u_id": "murat", "time": i*2}) for i in range(11)]
    
    for i in range(11):
        can_threads[i].start()
        murat_threads[i].start()


if __name__ == "__main__":
    test()


