import re

test_input = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

regex = r"Step ([A-Z]{1}) must be finished before step ([A-Z]{1}) can begin."

def parse_line(line):
    pre, post = re.match(regex, line).groups()
    return pre, post

def preconditions(requirements):
    steps = {step for req in requirements for step in req}

    preconds = {step: set() for step in steps}

    for pre, post in requirements:
        preconds[post].add(pre)

    return preconds

def find_order(requirements):
    order = []

    preconds = preconditions(requirements)

    while preconds:
        candidates = [step for step, reqs in preconds.items() if not reqs]

        next_item = min(candidates)
        order.append(next_item)

        for reqs in preconds.values():
            if next_item in reqs:
                reqs.remove(next_item)

        del preconds[next_item]

    return "".join(order)

data = [parse_line(line.strip("\n")) for line in open("input.txt").readlines()]
# data = [parse_line(line) for line in test_input.split("\n")]

# print(find_order(data))


class WorkItem():
    def __init__(self, worker_id, item, start_time, end_time):
        self.worker_id = worker_id
        self.item = item
        self.start_time = start_time 
        self.end_time = end_time

WORKERS_NO = 5


def time_step(step, base=60):
    return ord(step) - ord('A') + base + 1

def find_time(requirements, num_workers, base):

    preconds = preconditions(requirements)
    work_items = [None for _ in range(WORKERS_NO)]
    
    # Find the available workers
    time = 0
    while any(work_items) or preconds:

        # Check if anyone is one
        for i, work_item in enumerate(work_items):
            if work_item and work_item.end_time <= time:
                # Item is finished
                work_items[i] = None

                for reqs in preconds.values():
                    if work_item.item in reqs:
                        reqs.remove(work_item.item)

        # What are the available steps?
        candidates = [step for step, reqs in preconds.items() if not reqs]
        candidates = sorted(candidates, reverse=True)
        available_workers = [i for i in range(WORKERS_NO) if work_items[i] is None]

        # Assign work to worker
        while available_workers and candidates:
            worker_id = available_workers.pop()
            item = candidates.pop()

            work_items[worker_id] = WorkItem(
                worker_id,
                item,
                time,
                time + time_step(item, base)
            )
            del preconds[item]

        if any(work_items):
            time = min(work_item.end_time for work_item in work_items if work_item)
    return time



print(find_time(data, WORKERS_NO, 60))



