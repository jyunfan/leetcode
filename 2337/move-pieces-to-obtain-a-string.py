class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # check if order is correct
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        # check position possible
        n = len(start)
        R_start = list(map(lambda x: x[0], filter(lambda x: x[1]=='R', zip(range(n), start))))
        R_target = list(map(lambda x: x[0], filter(lambda x: x[1]=='R', zip(range(n), target))))
        #print(list(R_start), list(R_target))
        
        L_start = list(map(lambda x: x[0], filter(lambda x: x[1]=='L', zip(range(n), start))))
        L_target = list(map(lambda x: x[0], filter(lambda x: x[1]=='L', zip(range(n), target))))
        #print(list(L_start), list(L_target))

        R_correct = True if len(R_start)==0 else reduce(
                lambda x,y: x and y,
                map(lambda x: True if x[0] <= x[1] else False, zip(R_start, R_target))
        )
        L_correct = True if len(L_start)==0 else reduce(
                lambda x,y: x and y,
                map(lambda x: True if x[0] >= x[1] else False, zip(L_start, L_target))
        )
        Lmatch = list(map(lambda x: True if x[0] >= x[1] else False, zip(L_start, L_target)))
        return R_correct and L_correct
