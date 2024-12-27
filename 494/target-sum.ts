function findTargetSumWays(nums: number[], target: number): number {
    let m = new Map();  // key: sum, value: number of different expressions
    m.set(0, 1);        // at beginning we have only 1 way to get sum 0.
    for (let i = 0; i < nums.length; i++) { // add nums[i]
        let nm = new Map();
        for (let key of m.keys()) {
            nm.set(key + nums[i], m.get(key) + (nm.get(key + nums[i]) ?? 0));   // +nums[i]
            nm.set(key - nums[i], m.get(key) + (nm.get(key - nums[i]) ?? 0));   // -nums[i]
        }
        m = nm;
    }
    return m.get(target) ?? 0;
};
