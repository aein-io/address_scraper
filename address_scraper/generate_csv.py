# TODO: @aaron
from csv import DictWriter
from io import StringIO

from address import Address


def generate_csv(addresses: list[Address], flag=True) -> StringIO:
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

    if flag:
        csv_writer.writeheader()

    [csv_writer.writerow(address.dict()) for address in addresses]

    file.seek(0)
    return file
