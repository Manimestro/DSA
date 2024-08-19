//  [0,1,1,2,3,5,8,13,21]
// print 5th fib(5)
function fibonacci(n){
    let a = 0 
    let b = 1
    if (n==0) return 0
    if (n==1) return 1
    let i=1
    while (i<n){
        temp = a
        a = b
        b = temp+b
        i+=1
    }
   console.log(b)
}

fibonacci(5)

function Recfibonacci(n){
    if (n==1 || n==0){
        return n
    }
    let a = Recfibonacci(n-1)
    let b = Recfibonacci(n-2)
    return a+b
}
console.log(Recfibonacci(5))