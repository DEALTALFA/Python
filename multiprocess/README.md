# Multiprocessing vs Threading Map/Submit Example

This project demonstrates the differences between using `map()` and `submit()` methods in Python's multiprocessing and threading implementations.

## Key Differences

### Map
- Takes an iterable of inputs and applies same function to each input
- Returns results in order of inputs
- Blocks until all tasks complete
- Good for parallel operations on iterables where order matters

### Submit  
- Submits individual tasks asynchronously
- Returns Future objects immediately
- Non-blocking - can submit tasks while others are running
- Better for independent tasks that can run in any order

## Implementation Examples

### Multiprocessing

```python
# Map
with ProcessPoolExecutor() as executor:
    results = executor.map(function, iterable)
    
# Submit      # Using as_completed to get results in order of completion
with ProcessPoolExecutor() as executor:
    futures = [executor.submit(function, item) for item in iterable]
    results = [f.result() for f in as_completed(futures)]
# Multiprocessing vs Threading Map/Submit Example
```
## Key Differences

### Map
- Takes an iterable of inputs and applies same function to each input
- Returns results in order of inputs
- Blocks until all tasks complete
- Good for parallel operations on iterables where order matters

### Submit  
- Submits individual tasks asynchronously
- Returns Future objects immediately
- Non-blocking - can submit tasks while others are running
