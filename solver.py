from time import process_time
from state import State
import heapq

goalTest = [[0,1,2],[3,4,5],[6,7,8]]

class Solver:
	def __init__(self,initialState):
		self.initialState = initialState
		self.explored = set()
		self.depth = 0
		self.expandedNodes = 0
		


	def solve(self):
		start_time = process_time()
		queue = [self.initialState]
		self.initialState.getFManhattan()
		self.explored.add(self.initialState.id)
		while queue:
			self.expandedNodes += 1
			state = heapq.heappop(queue)
			if (state.board == goalTest):
				self.finalState = state
				self.runningTime = process_time() - 0
				return True
			if state.depth+1 > self.depth:
				self.depth = state.depth+1
			for neighbor in state.neighbors():
				if not ((neighbor.id in self.explored)):
					self.explored.add(neighbor.id)
					neighbor.getFManhattan()
					heapq.heappush(queue,neighbor)
		self.runningTime = process_time() - 0
		return False