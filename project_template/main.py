from app.io import output, input


def main():
    input_text_from_console = input.input_text_from_console()
    output.output_to_console(input_text_from_console + "  --> this is input to console function")
    output.output_to_file("data/build_in_capabilities.txt", input_text_from_console)
    output.output_to_file_with_pandas("data/panda_library.csv", input_text_from_console)
    output.output_to_console("Text was written to files")

    output.output_to_console("Read from file with build-in capabilities")
    file_content = input.input_text_from_file("data/build_in_capabilities.txt")
    output.output_to_console(f"Content of file --> {file_content}")

    output.output_to_console("Read from file with panda library")
    file_content = input.input_text_with_pandas("data/panda_library.csv")
    output.output_to_console(f"Content of pandas file --> {file_content}")


if __name__ == '__main__':
    main()
