function simpleadding (num) {
	res =0
	if (num.value < 1000 && num.value > 1) {
		for (var i = 1; i <= num.value; i++) {
			res   += parseInt(i);
		}
	}else
	{
		alert('Error number must be betwen 1 and 1000');
		num.value = "";
		return ;
	};
		console.log(res)
}