impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        fn is_palindrom(s: &[u8]) -> bool{
            s.iter().zip(s.iter().rev()).all(|(l,r)| l==r)
        }
        
        for size in (1..=s.len()).rev(){
            match s.as_bytes()
                .windows(size)
                .find(|substr| is_palindrom(substr)){
                    Some(pal) => return String::from_utf8(pal.to_vec()).unwrap(),
                    None => continue,
            }
        }
        String::from("")
        
    }
}