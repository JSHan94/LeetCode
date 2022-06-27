impl Solution {
    pub fn my_atoi(str: String) -> i32 {
        let (p, s) = match str.chars().skip_while(|x| x.is_whitespace()).take(1).next(){
            Some('+') => (1,1),
            Some('-') => (1,-1),
            Some(x) if x.is_digit(10) => (0,1),
            _ => return 0 ,
        };
        
        let mut res : i32 = 0;
        let overflow_res = if s > 0 {std::i32::MAX} else { std::i32::MIN };
        
        for c in str.chars().skip_while(|x| x.is_whitespace()).skip(p).take_while(|x| x.is_digit(10)){
            let (r,o) = res.overflowing_mul(10);
            if o {return overflow_res;}
            let (r,o) = r.overflowing_add(s*(c as i32 - '0' as i32));
            if o {return overflow_res;}
            res = r;
        }
        
        res
    }
}