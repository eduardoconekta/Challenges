def factorial
	p "ingresa un numero"
	factor=gets.chomp()
	res =1
	for i in (2..factor.to_i)
		res*=i
		p ">: #{res}"
	end
end

factorial