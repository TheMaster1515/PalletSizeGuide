# models/cargo_van.py
from .vehicles import Vehicle  # Ensure correct import of Vehicle

class Fiftythreefoot(Vehicle):
    def __init__(self):
        # Correctly call the __init__ method of the base class Vehicle
        super().__init__("Fiftythreefoot", (636, 100, 110), 43000)

    def check_fit(self, pallet_size, pallet_weight, total_weight, num_pallets, stackable):
        fit = self.can_fit(pallet_size, pallet_weight, total_weight)
        
        if not fit:
            fit, pallet_size[0], pallet_size[1], pallet_size[2], pallet_weight * num_pallets
        
        pallet_length, pallet_width, pallet_height = pallet_size
        total_length = pallet_length
        total_width = pallet_width
        total_height = pallet_height

        if pallet_height > 55 and pallet_width > 50:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("53 Stackable 48x51x56")             
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x51x56")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width > 50 and pallet_height <= 55:
            total_length = pallet_length 
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("53 Stackable 48x51x55")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets >= 3:
                    total_height = pallet_height * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x51x55")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width > 50 and pallet_height <= 36:
            total_length = pallet_length 
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("53 Stackable 48x51x36")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets >= 4:
                    total_height = pallet_height * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x51x36")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width > 50 and pallet_height <= 27:
            total_length = pallet_length 
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("53 Stackable 48x51x27")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets >= 5:
                    total_height = pallet_height * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x51x27")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width > 50 and pallet_height <= 22:
            total_length = pallet_length 
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("53 Stackable 48x51x22")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height = pallet_height * 5
                elif num_pallets >= 6:
                    total_height = pallet_height * 5
                    total_length_increments = (num_pallets - 1) //5 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x51x22")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width > 50 and pallet_height <= 18:
            total_length = pallet_length 
            total_width = pallet_width
            total_height = pallet_height
            if stackable:    
                print ("53 Stackable 48x51x18")
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
                elif num_pallets >= 7:
                    total_height = pallet_height * 6
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x51x18")
                if num_pallets >= 2:
                    total_length_increments = (num_pallets - 1) //1 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height > 55 and pallet_width <= 50:
            if stackable:    
                print ("53 Stackable 48x50x56")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x50x56")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 55 and pallet_width <= 50:
            if stackable:    
                print ("53 Stackable 48x50x55")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif  3 <= num_pallets <= 4:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 2
                elif num_pallets >= 5:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x50x55")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 36 and pallet_width <= 50:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x50x36")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 3
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x50x36")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 27 and pallet_width <= 50:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x50x27")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets >= 5:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 4
                    total_length_increments = (num_pallets - 1) //8 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x50x27")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 22 and pallet_width <= 50:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x50x22")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height = pallet_height * 5
                elif num_pallets >= 6:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 5
                    total_length_increments = (num_pallets - 1) //10 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x50x22")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 18 and pallet_width <= 50:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x50x18")
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
                elif num_pallets >= 7:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 6
                    total_length_increments = (num_pallets - 1) //12 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x50x18")
                if num_pallets >= 2:
                    total_width = pallet_width * 2
                    total_length_increments = (num_pallets - 1) //2 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height > 55 and pallet_width <= 33:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x33x56")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x33x56")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 33 and pallet_height <= 55:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x33x55")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif 3 <= num_pallets <= 4:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 2
                elif num_pallets >= 5:
                    total_width = pallet_width * 3
                    total_height = pallet_height * 2
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x33x55")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 33 and pallet_height <= 36:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x33x36")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif 4 <= num_pallets <= 6:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 2
                elif num_pallets >= 7:
                    total_width = pallet_width * 3
                    total_height = pallet_height * 3
                    total_length_increments = (num_pallets - 1) //9 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x33x36")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 33 and pallet_height <= 27:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x33x27")
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
            else:
                print ("53 Non-Stackable 48x33x27")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 33 and pallet_height <= 22:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x33x22")
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
            else:
                print ("53 Non-Stackable 48x33x22")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 33 and pallet_height <= 18:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x33x18")
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
            else:
                print ("53 Non-Stackable 48x33x18")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets >= 3:
                    total_width = pallet_width * 3
                    total_length_increments = (num_pallets - 1) //3 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height > 55 and pallet_width <= 25:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x25x56")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x25x56")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 25 and pallet_height <= 55:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x25x55")
                if num_pallets == 2:
                    total_length = pallet_height * 2
                elif 3 <= num_pallets <= 4:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 2
                elif 5 <= num_pallets <= 6:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 3
                elif num_pallets >= 7:
                    total_width = pallet_width * 4
                    total_height = pallet_height * 2
                    total_length_increments = (num_pallets - 1) //8 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x25x55")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 25 and pallet_height <= 36:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x25x36")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif 4 <= num_pallets <= 6:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 2
                elif 7 <= num_pallets <= 9:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 3
                elif num_pallets >= 10:
                    total_width = pallet_width * 4
                    total_height = pallet_height * 3
                    total_length_increments = (num_pallets - 1) //12 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x25x36")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 25 and pallet_height <= 27:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x25x27")
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
                    total_height = pallet_height * 4
                    total_width = pallet_width * 3
                elif num_pallets >= 13:
                    total_width = pallet_width * 4
                    total_height = pallet_height * 4
                    total_length_increments = (num_pallets - 1) //16 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x25x27")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 25 and pallet_height <= 22:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x25x22")
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
                    total_length_increments = (num_pallets - 1) //20 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x25x22")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 25 and pallet_height <= 18:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x25x18")
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
                    total_length_increments = (num_pallets - 1) //24 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x25x18")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets >= 4:
                    total_width = pallet_width * 4
                    total_length_increments = (num_pallets - 1) //4 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height > 55 and pallet_width <= 20:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x20x56")
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
                print ("53 Non-Stackable 48x20x56")
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
        if pallet_width <= 20 and pallet_height <= 55:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x20x55")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif 3 <= num_pallets <= 4:
                    total_width = pallet_width * 2
                    total_height = pallet_height * 2
                elif 5 <= num_pallets <= 6:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 3
                elif 7 <= num_pallets <= 8:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 4
                elif num_pallets >= 9:
                    total_width = pallet_width * 5
                    total_height = pallet_height * 2
                    total_length_increments = (num_pallets - 1) //10 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x20x55")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets >= 4:
                    total_width = pallet_width * 5
                    total_length_increments = (num_pallets - 1) //5 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 20 and pallet_height <= 36:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x20x36")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif 4 <= num_pallets <= 6:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 2
                elif 7 <= num_pallets <= 9:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 3
                elif 10 <= num_pallets <= 12:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 4
                elif num_pallets >= 13:
                    total_width = pallet_width * 5
                    total_height = pallet_height * 3
                    total_length_increments = (num_pallets - 1) //15 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x20x36")
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
        if pallet_width <= 20 and pallet_height <= 27:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x20x27")
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
                    total_height = pallet_height * 4
                    total_width = pallet_width * 3
                elif 13 <= num_pallets <= 16:
                    total_height = pallet_height * 4
                    total_width = pallet_width * 4
                elif num_pallets >= 17:
                    total_width = pallet_width * 5
                    total_height = pallet_height * 4
                    total_length_increments = (num_pallets - 1) //20 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x20x27")
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
        if pallet_width <= 20 and pallet_height <= 22:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x20x22")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height= pallet_height * 5
                elif 6 <= num_pallets <= 10:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 2
                elif 11 <= num_pallets <= 15:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 3
                elif 16 <= num_pallets <= 20:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 4
                elif num_pallets >= 21:
                    total_width = pallet_width * 5
                    total_height = pallet_height * 5
                    total_length_increments = (num_pallets - 1) //25 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x20x22")
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
        if pallet_width <= 20 and pallet_height <= 18:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x20x18")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif num_pallets == 4:
                    total_height = pallet_height * 4
                elif num_pallets == 5:
                    total_height= pallet_height * 5
                elif num_pallets == 6:
                    total_height = pallet_height * 6
                elif 7 <= num_pallets <= 12:
                    total_height = pallet_height * 6
                    total_width = pallet_width * 2
                elif 13 <= num_pallets <= 18:
                    total_height = pallet_height * 6
                    total_width = pallet_width * 3
                elif 19 <= num_pallets <= 24:
                    total_height = pallet_height * 6
                    total_width = pallet_width * 4
                elif num_pallets >= 25:
                    total_width = pallet_width * 5
                    total_height = pallet_height * 6
                    total_length_increments = (num_pallets - 1) //30 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x20x18")
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
        if pallet_height > 55 and pallet_width <= 16:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x16x56")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets == 5:
                    total_width = pallet_width * 5
                elif num_pallets >= 6:
                    total_width = pallet_width * 6
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x16x56")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets == 5:
                    total_width = pallet_width * 5
                elif num_pallets >= 6:
                    total_width = pallet_width * 6
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_height <= 55 and pallet_width <= 16:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x16x55")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif 3 <= num_pallets <= 4:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 2
                elif 5 <= num_pallets <= 6:
                    total_width = pallet_width * 3
                    total_height = pallet_height * 2
                elif 7 <= num_pallets <= 8:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 4
                elif 9 <= num_pallets <= 10:
                    total_height = pallet_height * 2
                    total_width = pallet_width * 5
                elif num_pallets >= 11:
                    total_width = pallet_width * 6
                    total_height = pallet_height * 2
                    total_length_increments = (num_pallets - 1) //12 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x16x55")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets == 5:
                    total_width = pallet_width * 5
                elif num_pallets >= 6:
                    total_width = pallet_width * 6
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 16 and pallet_height <= 36:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x16x36")
                if num_pallets == 2:
                    total_height = pallet_height * 2
                elif num_pallets == 3:
                    total_height = pallet_height * 3
                elif 4 <= num_pallets <= 6:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 2
                elif 7 <= num_pallets <= 9:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 3
                elif 10 <= num_pallets <= 12:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 4
                elif 13 <= num_pallets <= 15:
                    total_height = pallet_height * 3
                    total_width = pallet_width * 5
                elif num_pallets >= 16:
                    total_width = pallet_width * 6
                    total_height = pallet_height * 3
                    total_length_increments = (num_pallets - 1) //18 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x16x36")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets == 5:
                    total_width = pallet_width * 5
                elif num_pallets >= 6:
                    total_width = pallet_width * 6
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 16 and pallet_height <= 27:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x16x27")
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
                    total_height = pallet_height * 4
                    total_width = pallet_width * 3
                elif 13 <= num_pallets <= 16:
                    total_height = pallet_height * 4
                    total_width = pallet_width * 4
                elif 17 <= num_pallets <= 19:
                    total_height = pallet_height * 4
                    total_width = pallet_width * 5
                elif num_pallets >= 20:
                    total_width = pallet_width * 6
                    total_height = pallet_height * 4
                    total_length_increments = (num_pallets - 1) //24 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x16x27")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets == 5:
                    total_width = pallet_width * 5
                elif num_pallets >= 6:
                    total_width = pallet_width * 6
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 16 and pallet_height <= 22:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x16x22")
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
                elif 16 <= num_pallets <= 20:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 4
                elif 21 <= num_pallets <= 25:
                    total_height = pallet_height * 5
                    total_width = pallet_width * 5
                elif num_pallets >= 26:
                    total_width = pallet_width * 6
                    total_height = pallet_height * 5
                    total_length_increments = (num_pallets - 1) //30 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x16x22")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets == 5:
                    total_width = pallet_width * 5
                elif num_pallets >= 6:
                    total_width = pallet_width * 6
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments
        if pallet_width <= 16 and pallet_height <= 18:
            total_length = pallet_length
            total_width = pallet_width
            total_height = pallet_height
            if stackable:
                print ("53 Stackable 48x16x18")
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
                elif 19 <= num_pallets <= 24:
                    total_height = pallet_height * 6
                    total_width = pallet_width * 4
                elif 25 <= num_pallets <= 30:
                    total_height = pallet_height * 6
                    total_width = pallet_width * 5
                elif num_pallets >= 31:
                    total_width = pallet_width * 6
                    total_height = pallet_height * 6
                    total_length_increments = (num_pallets - 1) //36 + 1
                    total_length = pallet_length * total_length_increments
            else:
                print ("53 Non-Stackable 48x16x18")
                if num_pallets == 2:
                    total_width = pallet_width * 2
                elif num_pallets == 3:
                    total_width = pallet_width * 3
                elif num_pallets == 4:
                    total_width = pallet_width * 4
                elif num_pallets == 5:
                    total_width = pallet_width * 5
                elif num_pallets >= 6:
                    total_width = pallet_width * 6
                    total_length_increments = (num_pallets - 1) //6 + 1
                    total_length = pallet_length * total_length_increments


        length_check = total_length <= self.max_size[0]
        width_check = total_width <= self.max_size[1]
        height_check = total_height <= self.max_size[2]

        fit = fit and length_check and width_check and height_check

        # Debug output (optional)
        print(f"Debug Info - Total Length: {total_length}, Total Width: {total_width}, Total Height: {total_height}")

        return fit, total_length, total_width, total_height, pallet_weight * num_pallets
