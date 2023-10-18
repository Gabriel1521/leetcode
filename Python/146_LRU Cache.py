
# 146. LRU Cache

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.n = 0
        self.d = dict()
        self.q = collections.deque([])

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.n == 0:
            return -1
        else:
            if key in self.d:
                self.q.remove(key)
                self.q.append(key)
                return self.d[key]
            else:
                return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.n < self.c and key not in self.q:
            self.q.append(key)
            self.d[key] = value
            self.n += 1
        elif self.n < self.c and key in self.q:
            self.q.remove(key)
            self.q.append(key)
            self.d[key] = value
        elif self.n == self.c and key not in self.q:
            r = self.q.popleft()
            self.d.pop(r)
            self.q.append(key)
            self.d[key] = value
        elif self.n == self.c and key in self.q:
            self.d[key] = value
            self.q.remove(key)
            self.q.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
