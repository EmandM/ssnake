class Location:
    def __init__(self, x=0, y=0):
        self.x_coord = x
        self.y_coord = y

    # Method for creating a location from a location
    def create(self, location):
        self.x_coord = location.get_x()
        self.y_coord = location.get_y()
        return self

    def set_x(self, new):
        self.x_coord = new
    def get_x(self):
        return self.x_coord

    def set_y(self, new):
        self.y_coord = new
    def get_y(self):
        return self.y_coord

    def transform(self, adjustment):
        self.x_coord += adjustment
        self.y_coord += adjustment
        return self

    def get_location(self):
        return [self.x_coord, self.y_coord]



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__key() == other.__key()
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return hash(self.__key())
    def __key(self):
        return (self.x_coord, self.y_coord)
