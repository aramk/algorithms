from heapq import *
import itertools

class PriorityQueue:
	pq = []
	entry_finder = {}
	REMOVED = '<removed-task>'
	counter = itertools.count()  
	
	def __init__(self):
		pass

	def __repr__(self):
		s = ''
		for i in self.entry_finder:
			s += '%s: %s\n' % (str(i), str(self.entry_finder[i][0]))
		return s

	def push(self, task, priority=0):
	    'Add a new task or update the priority of an existing task'
	    if task in self.entry_finder:
	        self.__remove_task__(task)
	    count = next(self.counter)
	    entry = [priority, count, task]
	    self.entry_finder[task] = entry
	    heappush(self.pq, entry)

	def __remove_task__(self, task):
	    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
	    entry = self.entry_finder.pop(task)
	    entry[-1] = PriorityQueue.REMOVED

	def pop(self):
	    'Remove and return the lowest priority task. Raise KeyError if empty.'
	    while self.pq:
	        priority, count, task = heappop(self.pq)
	        if task is not PriorityQueue.REMOVED:
	            del self.entry_finder[task]
	            return task
	    raise KeyError('pop from an empty priority queue')

	def size(self):
		return len(self.entry_finder)
