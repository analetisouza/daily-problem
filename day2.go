package main

import "fmt"

func product_array(input_array []int) []int {

	result_array := []int{}

	for i := 0; i < len(input_array); i++ {
		temp := make([]int, len(input_array))
		copy(temp, input_array)
		temp = append(temp[:i], temp[i+1:]...)

		current_product := 1

		for j := 0; j < len(temp); j++ {
			current_product *= temp[j];
		}
		result_array = append(result_array, current_product)
	}
	return result_array
}

func main() {

	test1 := []int{1, 2, 3, 4, 5}
	test2 := []int{3, 2, 1}
    fmt.Println(product_array(test1))
	fmt.Println(product_array(test2))
}
