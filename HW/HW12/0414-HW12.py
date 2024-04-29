


def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
    # initialize a list to store all pipes
    all_pipes = [[0, i+1, well_cost] for i, well_cost in enumerate(wells)]  # Represent wells as pipes from the water source (node 0) to each house
    all_pipes.extend(pipes)

    #sort pipes based on cost in non-decreasing order
    all_pipes.sort(key = lambda x: x[2])

    #

