class Pattern:
    def __init__(self, base=5) -> None:
        self.base = base

    def diamond(self) -> str:
        diamond_arr = [ [' '] * self.base for _ in range(self.base) ]
        tot_row_len = self.base
        mid_pos = (self.base//2) + 1

        diamond_arr_idx = 0
        num_of_spaces = mid_pos -1
        for index in range(1, self.base+1, 2):
            for sub_ar_index in range(index):
                diamond_arr[diamond_arr_idx][sub_ar_index + num_of_spaces] = '*'
            num_of_spaces -= 1
            diamond_arr_idx += 1
            
            # find middle position
            # add left and right to middle
        
        j = 0
        for i in range(mid_pos):
            diamond_arr[mid_pos-1 + j] = diamond_arr[mid_pos-1-j]
            j +=1
    
        for row in diamond_arr:
            for el in row:
                print(el, end = '')
            print()


pat_obj = Pattern()
pat_obj.diamond()