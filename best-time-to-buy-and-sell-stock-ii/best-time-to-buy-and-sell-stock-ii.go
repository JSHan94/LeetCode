func maxProfit(prices []int) int {
    totalProfit, curMinIdx, ptr := 0, 0, 0
    for ; ptr < len(prices) ; ptr ++ {
        if prices[ptr] > prices[curMinIdx] {
            totalProfit += prices[ptr] - prices[curMinIdx]
            curMinIdx = ptr
        }
        if  prices[curMinIdx] > prices[ptr] {
            curMinIdx = ptr
        }
    }
    return totalProfit
}