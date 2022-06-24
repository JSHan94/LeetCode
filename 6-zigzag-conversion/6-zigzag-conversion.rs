impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows < 2 {
            return s.into() ;
        }
        let num_rows = num_rows as usize;
        let mut strs = vec![String::new() ; num_rows];
        let mut row = 0;
        let mut down = true;
        for c in s.chars(){
            strs[row].push(c);
            if down {
               row =  row + 1;
            }else{
               row =  row - 1;
            }
            if (row > 0 && row < num_rows-1) == down{
                down = true;
            }else{
                down = false;
            }
        }
        
        strs.concat()
        
    }
}