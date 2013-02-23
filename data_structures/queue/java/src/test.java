public class test {

    /**
     * @param args
     * @throws Exception 
     */
    public static void main(String[] args) throws Exception {
//        test1();
        test2();
    }

    private static void test1() throws Exception {
        Queue queue = new Queue(3);
        queue.push(1);
        queue.push(2);
        queue.push(3);
        System.out.println(queue.size());
        queue.push(4);
        System.out.println(queue.count());
        System.out.println(queue.size());
        
        System.out.println(queue.pop());
        System.out.println(queue.pop());
        System.out.println(queue.pop());
        System.out.println(queue.pop());
        System.out.println(queue.count());
        System.out.println(queue.size());
    }
    
    private static void test2() throws Exception {        
        Queue queue = new Queue(3);
        queue.push(1);
        System.out.println(queue.pop());
        queue.push(2);
        System.out.println(queue.pop());
        queue.push(3);
        System.out.println(queue.pop());
        queue.push(4);
        System.out.println(queue.pop());
        System.out.println(queue.count());
        System.out.println(queue.size());
    }

}
