class Node{
    constructor(data){
        this.data = data
        this.next = null
        this.prev = null
    }
}
 class LinkedList{
    constructor(){
        this.head = null
        this.tail = null
        this.size = 0
    }
    add_front(data){
        var new_node = new Node(data)
        if(this.head === null){
            this.head = new_node
            this.tail = new_node
        }
        else{
            var current = this.head
            this.head = new_node
            this.head.next = current
        }        
        this.size++
    }
    add_back(data){
        var new_node = new Node(data)
        if(this.head === null){
            this.head = new_node
            this.tail = new_node
        }
        else{
            new_node.prev = this.tail
            this.tail.next = new_node
            this.tail = new_node 
        }        
        this.size++
    }
    
}   
 module.exports = LinkedList



