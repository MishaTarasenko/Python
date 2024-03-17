def input_text_from_console():
    """
    Get console input and return entered string

    Examples:
        >>> input_text_from_console()
        Hello World

    Returns:
        str: entered string
    """
    pass


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
    pass


def input_text_with_pandas(file_path):
    """
        Read from a file using the pandas library

        Examples:
            >>> input_text_with_pandas(../data/test.txt)
            DataFrame of file

        Args:
            file_path (str): path to file

        Returns:
            DataFrame: Dataframe of file
        Raises:
            FileNotFoundError: if file does not exists
            ValueError: If the file format is invalid or cannot be parsed as a DataFrame
    """
    pass
