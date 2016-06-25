package main

import "fmt"

func reverse(s string) string {
	arr := []byte(s)
	length := len(s) - 1
	for i := length; i > -1; i-- {
		arr[length-i] = s[i]
	}
	return string(arr)
}

func main() {
	fmt.Println(reverse("hola"))

}

/*
func reverse(word string) string {

	var str = string(word)
	var c = ""
	for i := len(word) - 1; i > 0; i-- {
		for _,elem := str {

		}
		c := str[i]
		fmt.Println(c)
	}
	return elem

	/*var c = ""
	var str = string(word)
	for _, r := range str {
		c := string(r)
		fmt.Println(c)
	}
	return c*/
