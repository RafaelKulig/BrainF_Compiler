import sys, argparse

def brain_comp(code: str):
    """
    A simple Brainfuck interpreter that executes Brainfuck code provided as a string.

    Args:
        code (str): The Brainfuck code to interpret.

    Raises:
        SyntaxError: If there are unmatched brackets in the code.
        IndexError: If the tape pointer moves to a negative position.
        Exception: For any other errors that may occur during execution.
    """
    # Only keep valid Brainfuck characters
    code = ''.join(filter(lambda x: x in [',', '.', '>', '<', '+', '-', '[', ']'], code))
    
    tape = [0]
    loop_table = {}
    user_input = []
    stack = []
    index = 0

    # Preprocess loops and build jump table
    for ip, command in enumerate(code):
        if command == "[":
            stack.append(ip)
        elif command == "]":
            if not stack:
                raise SyntaxError(f"Unmatched ']' at position {ip}")
            start = stack.pop()
            loop_table[start] = ip
            loop_table[ip] = start

    if stack:
        raise SyntaxError("Unmatched '[' at position(s): " + ", ".join(map(str, stack)))

    ip = 0
    while ip < len(code):
        command = code[ip]
        if command == "+":
            tape[index] = (tape[index] + 1) % 256
        elif command == "-":
            tape[index] = (tape[index] - 1) % 256
        elif command == "<":
            index -= 1
            if index < 0:
                raise IndexError("Tape pointer moved to a negative position")
        elif command == ">":
            index += 1
            if index == len(tape):
                tape.append(0)
        elif command == ".":
            print(chr(tape[index]), end="")
        elif command == ",":
            if not user_input:
                user_input = list(input())
            if user_input:
                tape[index] = ord(user_input.pop(0))
            else:
                tape[index] = 0
        elif command == "[":
            if tape[index] == 0:
                ip = loop_table[ip]
        elif command == "]":
            if tape[index] != 0:
                ip = loop_table[ip]
        
        ip += 1


def main():
    parser = argparse.ArgumentParser(description="Brainfuck Interpreter")
    parser.add_argument("-f",help="Path to the Brainfuck .txt, .b or .bf file")
    args = parser.parse_args()
    try:
        if args.f is not None:
            with open(args.f,"r") as p:
                code = p.read()
        brain_comp(code)  # type: ignore
    except FileNotFoundError:
        print(f"File not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()