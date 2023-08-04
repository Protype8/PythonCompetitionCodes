import collections
class ListNode:
  def __init__(self, val=0, prev=None,next=None):
    self.val = val
    self.prev = prev
    self.next = next
class LinkedList:
  def __init__(self):
    self.left = ListNode(0)
    self.right = ListNode(0,prev=self.left)
    self.left.next = self.right
    self.map = {}
  def length(self):
    return len(self.map)
  def pushRight(self,val):
    node = ListNode(val,self.right.prev,self.right)
    self.map[val] = node
    self.right.prev = node
    node.prev.next = node
  def pop(self,val):
    if val in self.map:
      node = self.map[val]
      next,prev = node.next,node.prev
      next.prev = prev
      prev.next = next
      self.map.pop(val,None)
  def popLeft(self):
    res = self.left.next.val
    self.pop(self.left.next.val)
    return res
  def update(self,val):
    self.pop(val)
    self.pushRight(val)
class LFUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.count = 0
    self.valMap = {}
    self.countMap = collections.defaultdict(int)
    self.listMap = collections.defaultdict(LinkedList)
  def counter(self,key):
    cnt = self.countMap[key]
    self.countMap[key] += 1
    self.listMap[cnt].pop(key)
    self.listMap[cnt+1].pushRight(key)
    if(self.count == cnt and self.listMap[cnt].length() == 0):
      self.count+=1
  def get(self, key: int) -> int:
    if(not key in self.valMap):
      return -1
    self.counter(key)
    return self.valMap[key]
  def put(self, key: int, value: int) -> None:
    if self.capacity == 0:
      return
    if key not in self.valMap and len(self.valMap) == self.capacity:
      res  = self.listMap[self.count].popLeft()
      self.valMap.pop(res)
      self.countMap.pop(res)
    self.valMap[key] = value
    self.counter(key)
    self.count = min(self.count,self.countMap[key])
lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
lfu.get(1)
lfu.put(3, 3)
lfu.get(2)
lfu.get(3)
lfu.put(4, 4)
lfu.get(1)
lfu.get(3)
lfu.get(4)
