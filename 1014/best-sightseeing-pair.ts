function maxScoreSightseeingPair(values: number[]): number {
    let n = values.length
    let bestLeft = new Array(n).fill(0)
    bestLeft[0] = values[0]-1
    for (let i=1; i < n; i++) {
        bestLeft[i] = Math.max(values[i]-1, bestLeft[i-1]-1)
    }
    let max_score = 0
    for (let i=1; i < n; i++) {
        max_score = Math.max(max_score, bestLeft[i-1] + values[i]) 
    }
    return max_score
};
