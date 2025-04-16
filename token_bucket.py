
#!/usr/bin/env python

# tokens are inserted to the bucket at preset rates
# once the bucket is full no more tokens are added
#
import time

user_tokens = {}

def is_allowed(user_id, current_time = None):
    capacity, time_frame, remaining_token_count, last_deposit_time = user_tokens[user_id]
    current_time = time.now() if not current_time else current_time
    deposit_frame = min(current_time - last_deposit_time, time_frame)

    deposit_tokens = int(capacity * (deposit_frame / time_frame))
#     print(deposit_tokens)
    current_token_count = remaining_token_count + deposit_tokens - 1
    if current_token_count > 0:
        user_tokens[user_id] = (capacity, time_frame, current_token_count, current_time)
        return True

    return False


user_tokens[0] = (5, 10, 5, 0)

for i in range(1, 10):
    print(is_allowed(0, i))


