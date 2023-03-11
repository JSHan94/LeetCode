func removeDuplicates(nums []int) int {
    ptr1, ptr2, k := 0,0,0
    
    for ; ptr1 < len(nums) ; ptr1++{
        if ptr1 == 0 {
            k++
            continue
        }
        if nums[ptr1] != nums[ptr2] {
            ptr2++
            k++
            nums[ptr2] = nums[ptr1]
        }
    }
    return k
}