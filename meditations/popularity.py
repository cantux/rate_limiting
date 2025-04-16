"""

    void increasePopularity(Integer contentId);
    Integer mostPopular();
    void decreasePopularity(Integer contentId);

    
    Sample execution:
[
  popularityTracker.increasePopularity(7);
  popularityTracker.increasePopularity(7);
  popularityTracker.increasePopularity(8);
  popularityTracker.mostPopular();        // returns 7
  popularityTracker.increasePopularity(8);
  popularityTracker.increasePopularity(8);    # 8 3, 7 2 
  popularityTracker.mostPopular();        // returns 8
  popularityTracker.decreasePopularity(8);
  popularityTracker.decreasePopularity(8);    # 8 1, 7 2 
  popularityTracker.mostPopular();        // returns 7
  popularityTracker.decreasePopularity(7);
  popularityTracker.decreasePopularity(7);
  popularityTracker.decreasePopularity(8);
  popularityTracker.mostPopular();        // returns -1 since there is no content with popularity greater than 0
]

- there can be n many content

what happens when there is a tie? most recent touched upon
"""


# cotent_popularity: { content_id: popularity_count }
# popularity_content: {popularity_count: [content_id, content_id.. ] } O(number of different contents) -> maybe think about optimizing this

from collections import defaultdict, OrderedDict

class PopularityTracker:
    def __init__(self):
        self.content_popularity = defaultdict(int)
        self.popularity_content = defaultdict(OrderedDict)
        self.most_popular_count = 0
            
            
            
    def remove_from_previous_popularity(self, contentId):
        prev_content_popularity = 0
        if contentId in self.content_popularity:
            prev_content_popularity = self.content_popularity[contentId]
        
        # remove from the popularity content
        if prev_content_popularity in self.popularity_content:
            del self.popularity_content[prev_content_popularity][contentId]
        return prev_content_popularity
    
    def update_current_popularity(self, contentId, curr_content_popularity):
        self.content_popularity[contentId] = curr_content_popularity
        self.popularity_content[curr_content_popularity][contentId] = curr_content_popularity
        
        
    def increasePopularity(self, contentId):
        prev_content_popularity = self.remove_from_previous_popularity(contentId)
        
        curr_content_popularity = prev_content_popularity + 1
        
        self.update_current_popularity(contentId, curr_content_popularity)
        
        if curr_content_popularity > self.most_popular_count:
            self.most_popular_count = curr_content_popularity
        
    def mostPopular(self):
        if self.most_popular_count == 0:
            return -1
        else:
            # ordered_items = list(self.popularity_content[self.most_popular_count].od.ordered_items())
            return list(self.popularity_content[self.most_popular_count].items())[-1]
            # return ordered_items[-1]
        
    def decreasePopularity(self, contentId):
        prev_content_popularity = self.remove_from_previous_popularity(contentId)
                
        curr_content_popularity = prev_content_popularity - 1
        
        if not self.popularity_content[self.most_popular_count]:
            self.most_popular_count = curr_content_popularity
            
        self.update_current_popularity(contentId, curr_content_popularity)
        

def tests():
    popularityTracker = PopularityTracker()
    popularityTracker.increasePopularity(7)
    popularityTracker.increasePopularity(7)
    popularityTracker.increasePopularity(8)
    print(popularityTracker.mostPopular())        # returns 7
    popularityTracker.increasePopularity(8)
    popularityTracker.increasePopularity(8)    # 8 3, 7 2 
    print(popularityTracker.mostPopular())        # returns 8
    popularityTracker.decreasePopularity(8)
    popularityTracker.decreasePopularity(8)    # 8 1, 7 2 
    print(popularityTracker.mostPopular())        # returns 7
    popularityTracker.decreasePopularity(7)
    popularityTracker.decreasePopularity(7)
    popularityTracker.decreasePopularity(8)
    print(popularityTracker.mostPopular())  # -1
    
tests()
