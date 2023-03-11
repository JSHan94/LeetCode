func containsDuplicate(nums []int) bool {
    setNums := make(map[int]bool)
    for _,num := range nums{
        setNums[num] = true
    }
    return len(setNums) != len(nums)
    
}