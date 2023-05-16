# TODO: @aaron
from address import Address

from csv import DictWriter


def generate_csv(addresses: list[Address], filename: str) -> None:
    """
    Generate a CSV file from a list of addresses

    Args:
        addresses : list[Address]
            List of Address objects
        filename : str
            Name of the CSV file to be generated

    Returns:
        A reference to the CSV file generated
    """

    try:
        file = open(filename, 'w', newline='')
        fieldnames = addresses[0].schema()['properties'].keys()
    except (IndexError, FileNotFoundError) as e:
        raise e

    csv_writer = DictWriter(file, fieldnames=fieldnames)
    with file:
        csv_writer.writeheader()
        for address in addresses:
            csv_writer.writerow(address.dict())

    return file
