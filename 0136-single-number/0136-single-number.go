func singleNumber(nums []int) int {
    setNums := make(map[int]int)
    setSum, arrSum := 0, 0
    for _,num := range nums{
        setNums[num] = num
        arrSum += num
    }

    for _, setNum := range setNums {
        setSum += setNum
    }
    
    return 2*(setSum) - arrSum
}