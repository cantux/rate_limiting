
#!/usr/bin/env python

# add_route(path="foo", res="bar")
# call_route(path="foo")

class Trie:
    def __init__(self):
        self.mp = {}
    
    def insert(self, word, end_point):
        len_w = len(word)
        def int_insert(curr_node, char_idx):
            if char_idx == len_w:
                curr_node.mp["##"] = end_point
                return
            curr_char = word[char_idx]
            if curr_char not in curr_node.mp:
                curr_node.mp[curr_char] = Trie()
            int_insert(curr_node.mp[curr_char], char_idx + 1)
        int_insert(self, 0)

    def search(self, target):
        len_t = len(target)
        def int_search(search_node, target_idx):
            if target_idx == len_t:
                if "##" in search_node.mp:
                    return True, search_node.mp["##"]
                else:
                    return False, "no_such_route"
    
            found = False
            curr_char = target[target_idx]
            end_point = "no_such_route"
            if curr_char in search_node.mp:
                found, end_point = int_search(search_node.mp[curr_char], target_idx + 1)
            if not found and "*" in search_node.mp:
                found, end_point = int_search(search_node.mp["*"], target_idx)
            if not found and "*" in search_node.mp:
                found, end_point = int_search(search_node.mp["*"], target_idx + 1)
            if not found and "*" in search_node.mp:
                found, end_point = int_search(search_node, target_idx + 1)
            return found, end_point
        found, end_point = int_search(self, 0)
        return end_point

            
def test():
    router = Trie()
    assert "no_such_route" == router.search("foo")
    router.insert("foo", "foo_route")
    assert "foo_route" == router.search("foo")
    assert "no_such_route" == router.search("baz")
    router.insert("baz", "baz_route")
    assert "baz_route" == router.search("baz")
    assert "no_such_route" == router.search("bazo")
    router.insert("f*", "all_f_routes")
    assert "foo_route" == router.search("foo")
    assert "all_f_routes" == router.search("fooz")
    assert "all_f_routes" == router.search("fooasdf")
    print(router.search("f"))

if __name__ == "__main__":
    test()

