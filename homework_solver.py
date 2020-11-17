#
# Copyright DragonTechRoyale 2020
# usage:
# python3 homeworksolver.py /PATH/TO/questions.txt /PATH/TO/answers.txt
# Write all the questions in the regular format (like 1 * 290)
# You only need to provide the questions file
# .txt only
# This program has no warranty or support. Contact me on Twitter @DTR4K
#


import sys  # Import sys for using args


def main():
    try:
        input_file = open(sys.argv[1], "r")  # Try to open the input file in the string
    except range:
        print("Error: input a file")  # Print if unsuccessful
    try:
        output_file = open(sys.argv[2], "w")  # Try to create a string of the results
    except range:
        print("Error: input a file name to write to")
    print("Output file content:")
    for line in input_file.readlines():  # Go over all lines in the input file
        write_string = ""  # Create a string to write to
        if line != "\n" and line != "\r":  # If the line isn't a blank line
            write_string = line.rstrip('\r\n')  # Add to the string the content of the line (ex: 1+1)
            write_string = write_string + " = "  # Add to the string the equals to sign
            try:
                write_string = write_string + str(eval(line.rstrip('\r\n')))  # Try to calculate the string and add the
                # result to the string
            except ZeroDivisionError:
                write_string = write_string + "Error"  # If the calculation failed because of division by 0 Add "Error"
        else:
            write_string = write_string + "\n"  # Add an empty line to the string if it's an empty line
        print_string = write_string
        write_string = write_string + "\n"  # Add a line down to the string
        output_file.write(write_string)  # Write the string as a line to the output file
        print(print_string)
    input_file.close()  # Close the input file
    output_file.close()  # Close the output file


if __name__ == '__main__':
    main()
