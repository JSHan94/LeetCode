impl Solution {
    pub fn reverse(x: i32) -> i32 {
        println!("{:?}", x
            .abs()
            .to_string()
            .chars()
            .rev()
            .collect::<String>()
            .parse::<i32>()
            .unwrap_or(0));
        
        x.signum() * x
            .abs()
            .to_string()
            .chars()
            .rev()
            .collect::<String>()
            .parse::<i32>()
            .unwrap_or(0)
    }
}