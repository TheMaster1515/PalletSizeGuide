# models/cargo_van.py
from .vehicles import Vehicle  # Ensure correct import of Vehicle

class Twentyfoot(Vehicle):
    def __init__(self):
        # Correctly call the __init__ method of the base class Vehicle
        super().__init__("Twenty Foot", (240, 96, 96), 8500)

    def check_fit(self, pallet_size, pallet_weight, total_weight, num_pallets, stackable):
        fit = self.can_fit(pallet_size, pallet_weight, total_weight)
        
        if not fit:
            fit, pallet_size[0], pallet_size[1], pallet_size[2], pallet_weight * num_pallets
        
        pallet_length, pallet_width, pallet_height = pallet_size
        total_length = pallet_length
        total_width = pallet_width
        total_height = pallet_height

        if pallet_height > 48 and pallet_width > 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x49x49")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x49x49")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width > 48 and pallet_height <= 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x49x48")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets >= 3:
                    total_height = pallet_height * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x49x48")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments     
        if pallet_width > 48 and pallet_height <= 32:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x49x32")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets >= 3:
                    total_height = pallet_height * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x49x32")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments     
        if pallet_width > 48 and pallet_height <= 24:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x49x24")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets >= 4:
                    total_height = pallet_height * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x49x24")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments     
        if pallet_width > 48 and pallet_height <= 19:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x49x19")
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
            else:
                print ("Truck Non-Stackable 48x49x19")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments     
        if pallet_height > 48 and pallet_width <= 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x48x49")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x48x49")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 48 and pallet_width <= 48:
            total_height = pallet_height
            total_length = pallet_length
            total_width = pallet_width
            if stackable:    
                print ("Truck Stackable 48x48x48")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                if  3 <= num_pallets <= 4:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 2
                if num_pallets >= 5:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x48x48")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 48 and pallet_height <= 32:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x48x32")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif 4 <= num_pallets <= 6:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 2
                elif num_pallets >= 7:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x48x32")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments     
        if pallet_width <= 48 and pallet_height <= 24:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x48x24")
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
                    total_height = pallet_height * 4
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //8 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x48x24")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments     
        if pallet_width <= 48 and pallet_height <= 19:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x48x19")
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
                    total_height = pallet_height * 5
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //10 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x48x19")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments     
        if pallet_height > 48 and pallet_width <= 32:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x32x49")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x32x49")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 48 and pallet_width <= 32:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:   
                print ("Truck Stackable 48x32x48")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif 3 <=  num_pallets <= 4:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 2
                elif 5 <= num_pallets <= 6:
                    total_width = pallet_width * 3
                    total_height = pallet_height * 2
                elif num_pallets >= 7:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x32x48")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 32 and pallet_width <= 32:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:   
                print ("Truck Stackable 48x32x32")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif  num_pallets == 3:
                    total_height = pallet_height * 3
                elif 4 <= num_pallets <= 6:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 3
                elif num_pallets >= 7:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //9 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x32x32")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 24 and pallet_width <= 32:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:   
                print ("Truck Stackable 48x32x24")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif  num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif 5 <= num_pallets <= 8:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 4

                elif num_pallets >= 9:
                    total_height = pallet_height * 4
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //12 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x32x24")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 19 and pallet_width <= 32:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:   
                print ("Truck Stackable 48x32x19")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif  num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height = pallet_height * 5
                elif 6 <= num_pallets <= 10:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 5
                elif num_pallets >= 11:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //15 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x32x19")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height > 48 and pallet_width <= 24:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x24x49")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x24x49")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 24 and pallet_height <= 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x24x48")
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
            else:
                print ("Truck Non-Stackable 48x24x48")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 24 and pallet_height <= 32:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:   
                print ("Truck Stackable 48x24x32")
                if num_pallets == 2:
                    total_height = total_height * 2
                elif num_pallets == 3:
                    total_height = total_height * 3
                elif 4 <= num_pallets <= 6:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 2
                elif 7 <= num_pallets <= 9:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 3
                elif num_pallets >= 10:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //12 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x24x32")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif  num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 24 and pallet_width <= 24:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x24x24")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif  num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif 5 <= num_pallets <= 8:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 4
                elif 9 <= num_pallets <= 12:
                    total_width = pallet_width * 3
                    total_height = pallet_height * 4
                elif num_pallets >= 13:
                    total_height = pallet_height * 4
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //16 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x24x24")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 19 and pallet_width <= 24:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x24x19")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif  num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height = pallet_height * 5
                elif 6 <= num_pallets <= 10:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 5
                elif 11 <= num_pallets <= 15:
                    total_width = pallet_width * 3
                    total_height = pallet_height * 5
                elif num_pallets >= 16:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //20 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x24x19")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height > 48 and pallet_width <= 19:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x19x49")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets >= 5:
                    total_width = pallet_width * 5
                    total_length_increments = (num_pallets - 1) //5 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x19x49")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets >= 5:
                    total_width = pallet_width * 5
                    total_length_increments = (num_pallets - 1) //5 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 19 and pallet_height <= 48:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x19x48")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif 3 <= num_pallets <= 4:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 2
                elif 5 <= num_pallets <= 6:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 3
                elif 7 <= num_pallets <= 8:
                    total_width = pallet_width * 4
                    total_height = pallet_height * 2
                elif num_pallets >= 9:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 5
                    total_length_increments = (num_pallets - 1) //10 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x19x48")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets >= 5:
                    total_width = pallet_width * 5
                    total_length_increments = (num_pallets - 1) //5 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 19 and pallet_height <= 32:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:   
                print ("Truck Stackable 48x19x32")
                if num_pallets == 2:
                    total_height = total_height * 2
                elif num_pallets == 3:
                    total_height = total_height * 3
                elif 4 <= num_pallets <= 6:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 2
                elif 7 <= num_pallets <= 9:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 3
                elif 10 <= num_pallets <= 12:
                    total_width = pallet_width * 4
                    total_height = pallet_height * 3
                elif num_pallets >= 13:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 5
                    total_length_increments = (num_pallets - 1) //15 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x19x32")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets >= 5:
                    total_width = pallet_width * 5
                    total_length_increments = (num_pallets - 1) //5 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 19 and pallet_height <= 24:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:   
                print ("Truck Stackable 48x19x24")
                if num_pallets == 2:
                    total_height = total_height * 2
                elif num_pallets == 3:
                    total_height = total_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif 5 <= num_pallets <= 8:
                    total_height = pallet_height * 4
                    total_width = pallet_width * 2
                elif 9 <= num_pallets <= 12:
                    total_height = pallet_height * 4
                    total_width = pallet_width * 3
                elif 13 <= num_pallets <= 16:
                    total_width = pallet_width * 4
                    total_height = pallet_height * 4
                elif num_pallets >= 17:
                    total_height = pallet_height * 4
                    total_width = pallet_width * 5
                    total_length_increments = (num_pallets - 1) //20 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x19x24")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets >= 5:
                    total_width = pallet_width * 5
                    total_length_increments = (num_pallets - 1) //5 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 19 and pallet_width <= 19:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("Truck Stackable 48x19x19")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif  num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height = pallet_height * 5
                elif 6 <= num_pallets <= 10:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 5
                elif 11 <= num_pallets <= 15:
                    total_width = pallet_width * 3
                    total_height = pallet_height * 5
                elif 16 <= num_pallets <= 20:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 4
                elif num_pallets >= 21:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 5
                    total_length_increments = (num_pallets - 1) //25 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("Truck Non-Stackable 48x19x19")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets >= 5:
                    total_width = pallet_width * 5
                    total_length_increments = (num_pallets - 1) //5 + 1
                    total_length = pallet_length * total_length_increments


        length_check = total_length <= self.max_size[0]
        width_check = total_width <= self.max_size[1]
        height_check = total_height <= self.max_size[2]

        fit = fit and length_check and width_check and height_check

        # Debug output (optional)
        print(f"Debug Info - Total Length: {total_length}, Total Width: {total_width}, Total Height: {total_height}")

        return fit, total_length, total_width, total_height, pallet_weight * num_pallets
