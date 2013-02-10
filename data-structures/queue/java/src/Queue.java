
public class Queue {
    
    private static final int DEFAULT_SIZE = 20;
    
    private int queue[];
    private int size = 0;
    private int count = 0;
    private int start = 0;
    private int end = 0;
    
    public Queue() {
        this(DEFAULT_SIZE);
    }
    
    public Queue(int size) {
        queue = new int[size];
        this.size = size;
    }

    public boolean isFull() {
        return count == size;
    }
    
    public boolean isEmpty() {
        return count == 0;
    }
    
    public int count() {
        return count;
    }
    
    public int size() {
        return size;
    }
    
    public int pop() throws Exception {
        if (isEmpty()) {
            throw new Exception("Can't pop from empty queue");
        } else {
            int ret = queue[start];
            start = (start + 1) % size;
            count--;
            return ret;
        }
    }
    
    public void push(int value) {
        if (isFull()) {
            size *= 2;
            int[] copy = new int[size];
            for (int i = 0; i < count; i++) {
                copy[i] = queue[i];
            }
            queue = copy;
        }
        queue[end] = value;
        count++;
        end = (end + 1) % size;
    }
    
}
