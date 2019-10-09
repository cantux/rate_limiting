# rate_limiting
given a list of users, their limits, see if the user can continue with that request.

## Sliding log
keep a queue of requests and users. on every request, remove the elements that are not within the last hour.
Update the users' current limit users' limits are kept in a dictionary.

Alternatively keep requests of users in separate queues, remove the elements that are not within the last hour

One optimization is to only update the current request count when we hit the limit.
Another optimization is to use a index on the queue to search the time with extra O(n) space
Investigate use the fast pointer algorithm: http://www.ijcsit.com/docs/Volume%205/vol5issue02/ijcsit20140502215.pdf OR skip list??

Once the hour limit is found, drop all the elements before it.

### Complexity for each operation
Brute force: checks each entry in the queue. Tracking this in a db will introduce a huge response delay.
It makes sense to aim towards an in-memory centric application with scheduled backups for redundancy.

Losing cache locality with using a queue and a dictionary.
Consider implementing an extension module hash table and std::vector

### Probe for requirements
Findout about the metrics of user behavior:
Does the limit ever change, if not how often does the number of users change.

How to introduce a new user

Make some back of the envolope calculations assuming the profile of the requests.

Memory footprint looks like; 
for 1M users with 10K max limits: around ~80GB. sounds reasonable but how could we distribute the load?

## Remember CAP theorem: "a quick reCAP"
**consistency**: will all executions of reads and writes seen by all nodes be atomic or linearizably consistent.

**availability**: will a request made to the data store always eventually complete. 
System is said to be available iff all messages have a valid response but allows unbounded amount of delay.

**partition tolerence**: network(internal messaging between distributed data) is allowed to drop any messages. 
partiton ex: if the system is dependent on a single component and it fails, messages between some components will be lost/dropped.

CAP gaurantees that there is some circumstance(let's call it critical condition) in which a system must give up C or A. 
It doesn't say how likely the critical condition is. A single inconsistent read or unavailable write means that we reached it
Until critical condition system can be available and consistent.

You cannot build or choose partition tolerence.
if your system may experience partitions, you cannot always be C and A

YOU CANNOT CHOOSE IF YOUR SYSTEM WILL HAVE PARTITIONS. EITHER IT WILL OR IT WONT depending on the topology and dependence.
If you have a single application with a single dtabase, you can say you have partition tolerence but then it wouldn't be a distributed system eh
hence YOU CANNOT CA in distributed systems!! only cp or ap

Usually then, choose between consistency and availability.

Replicate data so that we have high availability, we now have the problem of synchronization.

Put some cache in front of it. Consider caching strategy. Keep a hot cache of more active users for example. Go nuts.

Put some smart routing(LB) depending on your users.

hw/vm elasticity / performance metrics? (auto instance invocation upon increased load)

Imagine wrapping this as a middleware.
If you want to globally limit the rates, simply introduce a single user. for group limiting, add groups as users

How to deploy this middleware?
Database migrations
Start with a single application server instance, monitor and make sure the behavior is matching the expected calculations slowly let it in.

### Further extend
Specify time frames for every limit but this version excludes them for brevity.

Reconsider load distribution if time frames and max rates change.


