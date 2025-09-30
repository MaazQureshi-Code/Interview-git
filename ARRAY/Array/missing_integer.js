




let arr = []

for(let num = 1; num <= 100; num++){

    if(num != 55){
          arr.push(num);
    }
}

const missingInteger = (A,n) => {
    let expectedNum =  n*(n+1)/2;
    let actualNum = A.reduce((a,b) => a+b,0);
    return expectedNum - actualNum
}

console.log(" This is missing integer " ,missingInteger(arr,100))