let nums = [3,1,2]
function subSeq(arr,n){
    if (n>=nums.length){
        console.log(arr)
        return 1
    }
    arr.push(nums[n])
    let take = subSeq(arr,n+1)
    arr.pop()
    let noTake = subSeq(arr,n+1)
    return take+noTake
}
console.log(`count ${subSeq([],0)}`)