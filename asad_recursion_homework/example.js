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

// printArr=(arr)=>{
//     if(arr.length === 0){
//         return
//     }    
//     printArr(slice_arr(0 ,arr.length-1, arr))
//     console.log(arr[arr.length-1])
// }


let array=[1,2,3,6]
console.log(array.slice(3))
console.log(slice_arr(array,3))