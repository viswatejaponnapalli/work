let myPromise=new Promise(function(myResolve,myReject){
    setTimeout(function(){
        myResolve("Data transfer done!");},3000);
    });
    myPromise.then(function(value){
        console.log("value is " +" "+value);
    });