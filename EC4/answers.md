1. Yes, we can definitely use heaps as priority queues. Using the nature of max heaps and min heaps, we can always return the root which would be the highest priority element of the queue. Inserting into the heap also calls heapify so it sorts itself in terms of highest to lowest priority.

```
function extractMin(heap):
    if heap.isEmpty():
        return None
    min_value = heap[0]
    heap[0] = heap.pop()
    heapifyDown(heap, 0)
    return min_value
```

```
function heapifyDown(heap, index):
    smallest = index
    leftChild = 2 * index + 1
    rightChild = 2 * index + 2

    if leftChild < heap.size() and heap[leftChild] < heap[smallest]:
        smallest = leftChild
    if rightChild < heap.size() and heap[rightChild] < heap[smallest]:
        smallest = rightChild

    if smallest != index:
        swap(heap[index], heap[smallest])
        heapifyDown(heap, smallest)
```
2. You definitely could use a max heap as a min heap and vice versa, but you would need to do some reversing when it comes to insertion and extraction. Inputting the negative of the values instead of the actual values and when we are extracting, we double negate it so the value returned is the original value.
```
function insertAsMin(heap, value):
    insertMaxHeap(heap, -value)  // Insert the negative of the value

function extractMin(heap):
    return -extractMax(heap)  // Extract the maximum (negated back)

function peekMin(heap):
    return -heap[0]  // Negate the root value to get the minimum
```
    
