  var fact=1,i;
function FirstFactorial(num){

    if(fact>0)fact=1;
    for (i=parseInt(num.value);i>0;i--)
    { fact*=i;
      console.log(fact);
    }
        //4*3*2*1
    //12 24 24 
    
};