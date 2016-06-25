function capitalize (str) {
	str = str.value
	str = str.replace(str[0],str[0].toUpperCase())
	for (var i = 0; i < str.length; i++) {
		if (str[i-1]==" ") {
			str = str.replace(str[i],str[i].toUpperCase())
		}
	}
	return str

}