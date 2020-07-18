const assert = require('assert')
const LinkedList = require('./linkedlist')

printLinkedListInReverse=(node)=>{
    if(node === null){
        return
    }
    printLinkedListInReverse(node.next)
    console.log(node.data)
} 

printLinkedList=(node)=>{
    if(node === null){
        return
    }
    console.log(node.data)
    printLinkedList(node.next)

}



var arr = []
print_0toN=(n)=>{
    if(n < 0){ 
        return//basecase}
    }
    print_0toN(n-1)//hypothesis
    arr.push(n)
    console.log(n)// induction
}


print_Negative_N_to_N=(n)=>{ 
    if(n < -N){
        return
    }
    else{
        
        print_Negative_N_to_N(n-1)//hypothesis
        console.log(n)// induction 
    }
}

slice_arr=(_array,start_index, end_index = _array.length)=>{
    let i = start_index
    let j = 0
    let _arr =[]
    while(i !== end_index){
     _arr[j] = _array[i]   
     ++j
     ++i
    }
    return _arr
}

printArr=(arr)=>{
    if(arr.length === 0){
        return
    }    
    printArr(slice_arr(arr, 0 ,arr.length-1))
    console.log(arr[arr.length-1])
}


printArrInReverse=(arr)=>{
    if(arr.length === 0){
        return
    }    
    
    console.log(arr[arr.length-1])
    printArrInReverse(slice_arr(arr, 0, arr.length-1))   
}

printSumArr = (arr)=>{
    if(arr.length === 0){
        return 0
    }    
    else{
        result = arr[0] + printSumArr(slice_arr(arr, 1)) // add all the items of arr except the first one and after that add the first element 
        return result
    }
}

isPalindrome=(str) =>{
    // base case #1
    if(str.length === 0 || str.length === 1 || (str.length === 2 && str[0] == slice_arr(str, -1))){
     return true;    
    }
    // base case #2
    if (str[0] !== slice_arr(str, -1)){
     return false;   
    }
    // recursive case
    return isPalindrome(slice_arr(str, 1, -1));     
}

printStringInReverse= (str)=>{
    if(str.length === 0){
        return
    }
    console.log(str[str.length-1])
    printStringInReverse(slice_arr(str, 0, str.length-1))    
}


// tests


// printStringInReverse("asad")





// var N=2
// print_Negative_N_to_N(N) // -2,-1,0,1,2







// print_0toN(4) // 0,1,2,3,4





let array =[1,2,3]

// printArrInReverse(array)


// printArr(array)



// assert.equal(printSumArr(array),6)
// console.log(printSumArr(array))



// let array1 = []
// assert.equal(printSumArr(array1), 0)
// console.log(printSumArr(array1))



// let array2 = [1,-2,-3]
// assert.equal(printSumArr(array2),-4)
// console.log(printSumArr(array2))



// assert.equal(isPalindrome("asffsa"),true)
// assert.equal(isPalindrome("asfrsa"),false)
// assert.equal(isPalindrome(""),true)
// assert.equal(isPalindrome("a"),true)
// assert.equal(isPalindrome("asad"),false)







// var linkedlist= new LinkedList()
// linkedlist.add_back(1) 
// linkedlist.add_back(2)
// linkedlist.add_back("3")
// linkedlist.add_back(4)

// printLinkedList(linkedlist.head)
// printLinkedListInReverse(linkedlist.head)