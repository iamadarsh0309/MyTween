class UserDocument:
    def __init__(self,first_name:str,last_name:str):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def get_or_create(cls,first_name:str,last_name:str)->"UserDocument":
        return cls(first_name,last_name)
