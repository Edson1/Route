import dataclasses

@dataclasses.dataclass
class RouteRequest:
    name: str = None
    data: str = None

    def to_dict(self):
        d =  {
            "name": self.name, 
            "data": self.data, 
        }
        return d

    @classmethod
    def from_dict(cls, data):
        return cls(
                name = data['name'],
                data = data['data'],
        )