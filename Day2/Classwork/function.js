let sum= (a,b)=>a+b;
let s=sum(5,6);
console.log(s+ " " + sum(20,100));
console.log("Callback Function");
function func2(num,callback){
    return callback(num);
}
const square=(n)=>n*n;
const cube=(a)=>a*a*a;
let ans=func2(6,square);
let ans_cube=func2(6,cube);
let ans_quad=func2(6,(n)=>n*n*n*n);
console.log(ans+ " "+ ans_cube + " " + ans_quad);


