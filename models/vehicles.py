# models/vehicles.py
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name, max_size, max_weight):
        self.name = name
        self.max_size = max_size
        self.max_weight = max_weight

    @abstractmethod
    def check_fit(self, pallet_size, pallet_weight, total_weight, num_pallets, stackable):
        """Check if the pallet fits in the vehicle."""
        pass

    def can_fit(self, pallet_size, pallet_weight, total_weight):
        """Check if the pallet's total weight and size fit in the vehicle."""
        pallet_length, pallet_width, pallet_height = pallet_size
        return (
            pallet_length <= self.max_size[0] and
            pallet_width <= self.max_size[1] and
            pallet_height <= self.max_size[2] and
            total_weight <= self.max_weight
        )

# Import specific vehicle classes here
from .cargo_van import CargoVan
from .sprinter import Sprinter
from .twelve_foot import Twelvefoot
from .fourteen_foot import Fourteenfoot
from .twenty_foot import Twentyfoot
from .twentyfour_foot import Twentyfourfoot
from .twentyeight_foot import Twentyeightfoot
from .fiftythree_foot import Fiftythreefoot
# Import other vehicle classes as needed

# Create instances of specific vehicles
vehicles = {
    "CargoVan": CargoVan(),
    "Sprinter Van": Sprinter(),
    "Twelve Foot": Twelvefoot(),
    "Fourteen Foot": Fourteenfoot(),
    "Twenty Foot": Twentyfoot(),
    "Twentyfour Foot": Twentyfourfoot(),
    "Twentyeight Foot": Twentyeightfoot(),
    "Fiftythree Foot": Fiftythreefoot(),
    # Instantiate other vehicle classes as needed
}
