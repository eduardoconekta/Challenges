
function reverse( word )
	word_complete=""
	res= string.len(word)
	for i=res,0,-1 do
		word_complete = word_complete..string.sub(word,i,i)
		-- (  ..  ) SE USAN PARA CONCATENAR
		print(string.sub(word,i,i))
	end
	print(word_complete)
end

--mandar a llamar la funcion
reverse("hola")