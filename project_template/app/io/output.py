import pandas as pd


def output_to_console(text):
    """
        Print text to console

        Examples:
            >>> output_to_console("Hello world")

        Args:
            text (str): Text printed to console

        Returns:
            None
    """
    print(text)


def output_to_file(file_path, data):
    """
        Writes text to a file using the built-in Python capabilities

        Examples:
            >>> output_to_file(../data/test.txt, "Hello world")

        Args:
            file_path (str): path to file to write to
            data (str): Text printed to file

        Returns:
            None
    """
    with open(file_path, "w") as file:
        file.write(data)


def output_to_file_with_pandas(file_path, data):
    """
            Writes text to a file using the pandas library

            Examples:
                >>> output_to_file_with_pandas(../data/test.txt, "Hello world")

            Args:
                file_path (str): path to file to write to
                data (str): Text printed to file

            Returns:
                None
        """
    data_to_df = {
        "text": [data]
    }
    df = pd.DataFrame(data_to_df)
    df.to_csv(file_path)

