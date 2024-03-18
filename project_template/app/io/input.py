import pandas as pd


def input_text_from_console():
    """
    Get console input and return entered string

    Examples:
        >>> input_text_from_console()
        Hello World

    Returns:
        str: entered string
    """
    user_input = input("")
    return user_input


def input_text_from_file(file_path):
    """
        Read from a file using built-in Python capabilities

        Examples:
            >>> input_text_from_console(../data/test.txt)
            Text from file

        Args:
            file_path (str): path to file

        Returns:
            str: content of the file

        Raises:
            FileNotFoundError: if file does not exists
    """
    with open(file_path) as file:
        return file.read()


def input_text_with_pandas(file_path):
    """
        Read from a file using the pandas library

        Examples:
            >>> input_text_with_pandas(../data/test.txt)
            Text from file

        Args:
            file_path (str): path to file

        Returns:
            str: content of the file
        Raises:
            FileNotFoundError: if file does not exists
            ValueError: If the file format is invalid or cannot be parsed as a DataFrame
    """
    df = pd.read_csv(file_path)
    return df.get("text")[0]
