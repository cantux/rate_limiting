
#!/usr/bin/env python
import heapq

class Ledger:
    def __init__(self):
        self.bids_h = []
        self.asks_h = []
        self.sorted_bids = []
        self.sorted_asks = []

    def add_ask(self, ask_val, ask_time, ask_owner):
        if self.bids[0][0] * -1 > ask: # there are bids higher than price offered
            bid_val, bid_time, bid_owner = heapq.heappop(self.bids)
        else:
            heapq.heappush(self.asks, (ask_val, ask_time, ask_owner))

    def add_bid(self, bid_val, bid_time, bid_owner):
        pass



def fnc():
    return None

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

