import itertools 

class Order:
    STATUS_UNKNOWN = 0
    STATUS_NEW = 1
    STATUS_FILLED = 2
    id = itertools.count()
    TYPE_UNKNOWN = "unknown"
    TYPE_BUY = "buy"
    TYPE_SELL = "sell"

    def __init__(self, limit_price, num_contracts, type=Order.TYPE_UNKNOWN, ):
        self.status = Order.STATUS_UNKNOWN
        self.id = next(Order.id)
        self.type = type
        self.limit_price = limit_price
        self.num_contracts = num_contracts
        self.remaining_contracts = num_contracts


class DocDB:
    def __init__(self):
        self.store = {}

class ContractMatch:

    counter = itertools.count() 
    def __init__(self, db):
        self.db = db

    def commit(self, order):
        store = self.db.store
        if order.type == "buy":
            match_count = 0
            store["sell_ledger"].sort(reverse=True)
            i = len(store["sell_ledger"]) - 1

            while i >= 0 and store["sell_ledger"][i].limit_price < order.limit_price and order.remaining_contracts > 0:
                available_sell = store["sell_ledger"][i]

                # case 1: we have more orders than available contracts

                #### remove from sell ledger and reduce order.remaining_contracts
                if order.remaining_contracts <= available_sell.remaining_contracts:
                    available_sell.remaining_contracts -= order.remaining_contracts
                    order.remaining_contracts = 0
                    # record this to executed contracts
                    if available_sell.remaining_contracts:
                        # remove from sell ledger
                        self.db.store["sell_ledger"].pop()
                else:
                    available_sell.remaining_contracts = 0
                    store["sell_ledger"].pop()
                    order.remaining_contracts -= available_sell.remaining_contracts
                    # record this to executed contracts
                i -= 1

            if order.remaining_contracts: # orders couldn't be fulfilled
                store["buy_ledger"].append(order)
        elif order.type == "sell":
            pass
        else: # unknown order type smt wrong
            pass

        # try to fill the new order
        self.id = next(ContractMatch.counter)


def test():
    doc_db = DocDB()

    cm = ContractMatch()

    # new buy orders coming in
    buy_five_for_fifteen = Order("sell", 5, 15)
    doc_db.store["orders"][buy_five_for_fifteen.id] = buy_five_for_fifteen

    cm.commit(buy_five_for_fifteen)

    [buy_five_for_fifteen.id]

    # new sell orders coming in
    buy_five_for_fifteen = Order("buy", 3, 16)
    buy_five_for_fifteen = Order("buy", 3, 16) # -> just fulfill 2 orders for 15 -> leave a remaining order open


    assert True

if __name__ == "__main__":
    test()

"""
ledger opiniated behavior

example:
sell order for 15
buy order for 16
define behavior: do we match them at 15? what do we with the remaining balance?

buy order exists for 16
new sell order coming in at 15

sell order existed before for 16
sell order for 15
new buy order coming in for 16 -> do we match with 15 or 16? what's the precedence? -> assumption: fill smallest or largest values
"""