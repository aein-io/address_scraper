# TODO: @aaron
from csv import DictWriter
from io import StringIO

from address import Address


def generate_csv(addresses: list[Address]) -> StringIO:
    """
    Generate a CSV file from a list of addresses

    Args:
        addresses : list[Address]
            List of Address objects

    Returns:
        A reference to the CSV file generated
    """

    try:
        file: StringIO = StringIO()
        fieldnames: dict.keys = addresses[0].schema()['properties'].keys()
    except (IndexError, FileNotFoundError) as e:
        raise e

    csv_writer: DictWriter = DictWriter(file, fieldnames=fieldnames)
    # with file:
    csv_writer.writeheader()
    for address in addresses:
        csv_writer.writerow(address.dict())

    file.seek(0)
    return file
