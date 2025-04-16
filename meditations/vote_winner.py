
#!/usr/bin/env python
from collections import defaultdict

def find_winner(ballot):
    # follow up 
    # how to resolve ties, sorted by alphabet, the number of 3 points, 
    ## by who reaches 70 points first
    # stream getwinner in O(1)

    team_vote = defaultdict(int)
    seen = {}
    for voter, team in ballot:
        if voter not in seen:
            team_vote[team] += 3
            seen[voter] = 2
        elif seen[voter] > 0 :
            team_vote[team] += self.seen[voter]
            seen[voter] -= 1

    return list(sorted([(vote_count, team) for team, vote_count in mp.items()]))[-1]

class TeamNode:
    def __init__(self, val=[]):
        self.prev = None
        self.next = None
        self.val = val

class TeamDLL:
    def __init__(self):
        self.head = TeamNode()
        self.tail = TeamNode()
        self.head.prev = self.tail
        self.head.next = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head

class TeamLRU:
    def __init__(self):
        self.team_mp = {}
        self.dll = TeamDLL()

    def add(self, val):
        new_node = TeamNode(val)
        self.team_mp[val[3]] = new_node
        prev_end = self.tail.prev
        prev_end.next = new_node
        new_node.prev = prev_end
        new_node.next = tail
        tail.prev = new_node
    
    def remove(self, team):
        to_remove = self.team_mp[team]
        next_node = to_remove.next
        prev_node = to_remove.prev
        next_node.prev = prev_node
        prev_node.next = next_node
        
class VoteTeamLRU:
    def __init__(self):
        self.vote_teamlru = {}

    def remove(self, prev_vote ,team):
        team_lru = self.vote_teamlru[prev_vote]
        team_lru.remove(team)

    def add(self, new_vote, val):
        if new_vote not in self.vote_teamlru:
            self.vote_teamlru[new_vote] = TeamLRU()
        self.vote_teamlru[new_vote].add(val[4])

def find_winner_quick(ballot):
    team_vote = defaultdict(int)
    vote_team = VoteTeamLRU()

    teams_uniq = set()
    for team, _ in ballot:
        if team not in teams_uniq:
            teams_uniq.add(team)
    
    for team in teams_uniq:
        team_vote[team] = 0
        vote_team.add(0, [0, 0, 0, 0, team])

    max_vote = -1
    for team, vote in ballot:
        prev_vote = team_vote[team]
        vote_team[prev_vote].remove(team)
        team_vote[team] += vote
        vote_team[team_vote[team]].append(team)
        

        
def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

