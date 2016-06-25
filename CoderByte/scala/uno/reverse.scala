    object reverse {
    	def reverse(word: String) = {
    		val res = word.toArray
			for( i <- res.length-1 to 0 by -1){
			    print(res(i));
			}
    	}
	    def main(args: Array[String]) {
	    	reverse("hola")
	    	println ("")
    	}
    }
