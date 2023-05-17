from csv import DictWriter
from io import StringIO


def generate_csv(addresses: list, flag=True) -> StringIO:
    """
    Generate a CSV file from a list of addresses.

    Args:
        addresses (list): List of Address objects.

    Raises:
        IndexError

    Returns:
        A reference to the CSV file generated.
    """

    try:
        file: StringIO = StringIO()
        fieldnames = addresses[0].schema()["properties"].keys()
    except IndexError as e:
        raise e

    csv_writer: DictWriter = DictWriter(file, fieldnames=fieldnames)

    if flag:
        csv_writer.writeheader()

    [csv_writer.writerow(address.dict()) for address in addresses]

    file.seek(0)
    return file
