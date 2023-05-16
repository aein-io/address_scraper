from pydantic import BaseModel


class Address(BaseModel):
    """
    Address dataclass that corresponds to a US address

    ...

    Attributes
    ----------
    city : str
    line : str
    street_name : str
    street_number : str
    street_suffix : str
    country : str
    postal_code : str
    state_code : str
    state : str
    lat : float
    lon : float
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
        strict_types = True
        orm_mode = True
        allow_mutation = False
