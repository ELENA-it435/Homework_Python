from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address      # экземпляр Address
        self.from_address = from_address  # экземпляр Address
        self.cost = cost
        self.track = track
            