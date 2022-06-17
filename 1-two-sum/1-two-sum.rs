impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;
        let _len = nums.len();
        let mut dict = HashMap::new();
        for (idx, value) in nums.into_iter().enumerate(){
            let expected_sum = target-value;
            match dict.get(&expected_sum){
                Some(&prev) => return vec![prev as i32, idx as i32],
                _ => {
                    dict.insert(value,idx);
                }
            }
        }
        unreachable!()
    }
}