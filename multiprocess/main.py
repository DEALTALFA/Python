
# Example demonstrating differences between map() and submit() in threading/processing

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from random import randint
import time

def process_item(x):
    # Simulate some work
    time.sleep(x)
    return f"slept for {x} sec"

def main():
    data = [3,4,5,7,1,6,9]
    
    # Using map with ThreadPoolExecutor
    print("# ThreadPoolExecutor with map()")
    with ThreadPoolExecutor(max_workers=4) as executor:
        # map() processes items in order, returns iterator
        results = executor.map(process_item, data)
        # Results are returned in same order as input
        print([r for r in results])

    # Using submit with ThreadPoolExecutor 
    print("\n# ThreadPoolExecutor with submit()")
    with ThreadPoolExecutor(max_workers=4) as executor:
        # submit() schedules individual tasks, returns Future objects
        futures = [executor.submit(process_item, x) for x in data]
        # Using as_completed to get results in order of completion
        results = [future.result() for future in as_completed(futures)]
        print(results)

    # Using map with ProcessPoolExecutor
    print("\n# ProcessPoolExecutor with map()")
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(process_item, data)
        print([r for r in results])

    # Using submit with ProcessPoolExecutor
    print("\n# ProcessPoolExecutor with submit()")
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(process_item, x) for x in data]
        # Using as_completed to get results in order of completion
        results = [future.result() for future in as_completed(futures)]
        print(results)

if __name__ == '__main__':
    main()

# Key differences shown:
# 1. map() maintains input order, submit() returns results as they complete
# 2. map() returns iterator, submit() returns Future objects
# 3. map() is simpler for straightforward parallel operations
# 4. submit() offers more control and flexibility for complex tasks