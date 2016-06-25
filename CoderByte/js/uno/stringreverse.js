var word=[],a='';
function stringreverse(str)
{

	word=str.split('');

	for (var i = str.length -1; i >= 0; i--) 
	{
		a+=word[i];
		
	};

	console.log(a);


}