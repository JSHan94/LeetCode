impl Solution {
    pub fn reverse_words(s: String) -> String {
        let s = s.split_whitespace();
        let mut res = String::from("");
        for (idx, item) in s.rev().enumerate(){
            if idx != 0 {
                res.push_str(&" ");
            }
            res.push_str(&item);
        }
        res
    }
}