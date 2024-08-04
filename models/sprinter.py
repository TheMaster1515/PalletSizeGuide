from .vehicles import Vehicle
class Sprinter(Vehicle):
    def __init__(self):
        super().__init__("Sprinter", (144, 48, 68), 3000)

    def check_fit(self, pallet_size, pallet_weight, total_weight, num_pallets, stackable):
        fit = self.can_fit(pallet_size, pallet_weight, total_weight)
        
        if not fit:
            fit, pallet_size[0], pallet_size[1], pallet_size[2], pallet_weight * num_pallets
        
        pallet_length, pallet_width, pallet_height = pallet_size
        total_length = pallet_length
        total_width = pallet_width
        total_height = pallet_height

        if pallet_height > 68 and pallet_width > 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x49x69")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x49x69")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 68 and pallet_width > 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x49x68")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x49x68")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 34 and pallet_width > 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x49x34")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x49x34")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 22 and pallet_width > 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x49x22")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x49x22")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 17 and pallet_width > 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x49x17")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x49x17")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 13 and pallet_width > 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x49x13")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x49x13")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 11 and pallet_width > 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x49x11")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x49x11")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height > 68 and pallet_width <= 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x48x69")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x48x69")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 48 and pallet_height <= 68:  
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x48x68")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x48x68")   
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 34 and pallet_width <= 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            print ("Van Stackable 48x48x34")
            if stackable:
                if num_pallets >= 2:
                    total_height = pallet_height * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x48x34")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 22 and pallet_width <= 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x48x22")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets >= 3:
                    total_height = pallet_height * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x48x22")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 48 and pallet_height <= 17:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x48x17")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets >= 4:
                    total_height = pallet_height * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x48x17")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 13 and pallet_width <= 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x48x13")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets >= 5:
                    total_height = pallet_height * 5
                    total_length_increments = (num_pallets - 1) //5 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x48x13")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 11 and pallet_width <= 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x48x11")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height = pallet_height * 5
                elif num_pallets >= 6:
                    total_height = pallet_height * 6
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x48x11")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height > 68 and pallet_width <= 24:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x24x69")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x24x69")  
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 24 and pallet_height <= 68:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Van Stackable 48x24x68")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x24x68")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 34 and pallet_width <= 24:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x24x34")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets >= 3:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x24x34")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 22 and pallet_width <= 24:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x24x22")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets >= 4:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x24x22")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 17 and pallet_width <= 24:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x24x17")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets >= 5:
                    total_height = pallet_height * 4
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //8 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x24x17")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 13 and pallet_width <= 24:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x24x13")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets >= 5:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //10 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x24x13")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 11 and pallet_width <= 24:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x24x11")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height = pallet_height * 5
                elif num_pallets >= 6:
                    total_height = pallet_height * 6
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //12 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x24x11")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height > 68 and pallet_width <= 16:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x16x69")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x16x69")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 16 and pallet_height <= 68:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x16x68")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x16x68")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 34 and pallet_width <= 16:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x16x34")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif 3 <= num_pallets <= 4:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 2
                elif num_pallets >= 5:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x16x34")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 22 and pallet_width <= 16:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x16x22")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif 4 <= num_pallets <= 6:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 2
                elif num_pallets >= 7:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //9 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x16x22")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 17 and pallet_width <= 16:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x16x17")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif 5 <= num_pallets <= 8:
                    total_height = pallet_height * 4
                    total_width = pallet_width * 2
                elif num_pallets >= 9:
                    total_width = pallet_width * 3
                    total_height = pallet_height * 4
                    total_length_increments = (num_pallets - 1) //12 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x16x17")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 13 and pallet_width <= 16:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x16x13")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height = pallet_height * 5
                elif 6 <= num_pallets <= 10:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 2
                elif num_pallets >= 11:
                    total_width = pallet_width * 3
                    total_height = pallet_height * 5
                    total_length_increments = (num_pallets - 1) //15 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x16x13")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 11 and pallet_width <= 16:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x16x11")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height = pallet_height * 5
                elif num_pallets == 6:
                    total_height = pallet_height * 6
                elif 7 <= num_pallets <= 12:
                    total_height = pallet_height * 6
                    total_width = pallet_width * 2
                elif num_pallets >= 13:
                    total_width = pallet_width * 3
                    total_height = pallet_height * 6
                    total_length_increments = (num_pallets - 1) //18 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x16x11")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height > 68 and pallet_width <= 12:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x12x69")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x12x69")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 12 and pallet_height <= 68:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x12x68")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x12x68")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 34 and pallet_width <= 12:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x12x34")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif 3 <= num_pallets <= 4:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 2
                elif 5 <= num_pallets <= 6:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 3
                elif num_pallets >= 7:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //8 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x12x34")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 22 and pallet_width <= 12:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x12x22")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif 4 <= num_pallets <= 6:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 2
                elif 7 <= num_pallets <= 9:
                    total_width = pallet_width * 3
                    total_height = pallet_height * 3
                elif num_pallets >= 10:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //12 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x12x22")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 17 and pallet_width <= 12:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("Van Stackable 48x12x17")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif 5 <= num_pallets <= 8:
                    total_height = pallet_height * 4
                    total_width = pallet_width * 2
                elif 9 <= num_pallets <= 12:
                    total_width = pallet_width * 3
                    total_height = pallet_height * 4
                elif num_pallets >= 13:
                    total_width = pallet_width * 4
                    total_height = pallet_height * 4
                    total_length_increments = (num_pallets - 1) //16 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print ("Van Non-Stackable 48x12x17")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments



        if pallet_height <= 13 and pallet_width <= 12:
            if stackable:
                print("Van Stackable 48x12x13")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height = pallet_height * 5
                elif 6 <= num_pallets <= 10:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 2
                elif 11 <= num_pallets <= 15:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 3
                elif num_pallets >= 16:
                    total_width = pallet_width * 4
                    total_height = pallet_height * 5
                    total_length_increments = (num_pallets - 1) // 20 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print("Van Non-Stackable 48x12x13")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) // 4 + 1
                    total_length = pallet_length * total_length_increments

        if pallet_height <= 11 and pallet_width <= 12:
            if stackable:
                print("Van Stackable 48x12x11")
                print(total_length)
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height = pallet_height * 5
                elif num_pallets == 6:
                    total_height = pallet_height * 6
                elif 7 <= num_pallets <= 12:
                    total_height = pallet_height * 6
                    total_width = pallet_width * 2
                elif 13 <= num_pallets <= 18:
                    total_height = pallet_height * 6
                    total_width = pallet_width * 3
                elif num_pallets >= 19:
                    total_width = pallet_width * 4
                    total_height = pallet_height * 6
                    total_length_increments = (num_pallets - 1) // 24 + 1
                    total_length = pallet_length * total_length_increments
            if not stackable:
                print("Van Non-Stackable 48x12x11")
                print(total_length)
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) // 4 + 1
                    total_length = pallet_length * total_length_increments

        length_check = total_length <= self.max_size[0]
        width_check = total_width <= self.max_size[1]
        height_check = total_height <= self.max_size[2]

        fit = fit and length_check and width_check and height_check

        # Debug output (optional)

        return fit, total_length, total_width, total_height, pallet_weight * num_pallets
