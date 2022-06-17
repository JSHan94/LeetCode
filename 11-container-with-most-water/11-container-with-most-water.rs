impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut iter = height.iter().enumerate();
        let (mut p1, mut p2) = (iter.next(), iter.next_back());
        while let (Some((i, h1)), Some((j,h2))) = (p1,p2){
            res = res.max(h1.min(h2) * (j-i) as i32);
            if h1 < h2 {
                p1 = iter.next();
            }else{
                p2 = iter.next_back();
            }
        }
        res
    }
}