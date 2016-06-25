word   = ""
save   = ""
bigger = 0
contador = 0
function Longestring (str) {
var st = str.value.split('')
	for (var i = 0 ; i <= str.value.length-1; i++) {
		if (st[i]== ' ') {
			console.log("=========Space==========")
			contador = 0
			word     = ""
		}else{
			contador++
			console.log("Counting..."+contador)
			word  += st[i];
			bigger = (contador>bigger)?contador:bigger;
			save   = (word.length>=bigger)?word:save;
		}
	}
			console.log("Your Word  "+save+" gets #"+bigger)
}