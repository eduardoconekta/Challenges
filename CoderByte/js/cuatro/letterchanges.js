var abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o',
'p','q','r','s','t','u','v','x','y','z']
function letterchange (str) {
	var aux = str.value.split("");
	for (var i = 0; i < aux.length; i++) {
		var index  = aux[i]
			num    = abc.indexOf(aux[i])
			num   +=1
			aux[i] = abc[num]
		if (aux[i]== 'a' ||aux[i] == 'e'|| aux[i] == 'i'|| aux[i] == 'o'||aux[i] == 'u' ) {
			aux[i] = aux[i].toUpperCase()
		};
	};
	console.log(String(aux))
}