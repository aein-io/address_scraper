from pydantic import BaseModel


class Address(BaseModel):
    """
    Address dataclass that corresponds to a US address.

    Attributes:
        city (str): The city of the Address.
        line (str): The street name, number, and suffix of the Address.
        street_name (str): The street name of the Address.
        street_number (str): The street number of the Address.
        street_suffix (str): The street suffix of the Address.
        country (str): The country of the Address.
        postal_code (str): The postal code of the Address.
        state_code (str): The state code of the Address.
        state (str): The state of the Address.
        coordinates (str): The coordinates of the Address.
        lat (float): The latitude of the Address.
        lon (float): The longitude of the Address.
    """

    city: str
    line: str
    street_name: str
    street_number: str
    street_suffix: str
    country: str
    postal_code: str
    state_code: str
    state: str
    coordinates: str
    lat: float
    lon: float

    class Config:
        """
        Configuration class for Address.

        Attributes:
            strict_types (bool): Enforces type checking.
            orm_mode (bool): Allows for better integration with ORMs.
            allow_mutation (bool): Enables or disables mutation of data.
        """

        strict_types = True
        orm_mode = True
        allow_mutation = False
