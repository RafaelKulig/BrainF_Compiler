# Brainfuck Interpreter in Python

This is a simple Brainfuck interpreter written in Python. It parses and executes Brainfuck code with support for all 8 standard Brainfuck commands.

## 💡 Features

- Full support for Brainfuck commands: `+ - < > [ ] , .`
- Memory tape with dynamic growth
- Loop matching with proper bracket validation
- Input handling (via `input()`)
- Wrap-around for 8-bit cell values (0–255)
- Error messages for unmatched brackets and invalid pointer movement

## 🧠 How It Works

1. Filters out any characters that are not valid Brainfuck instructions.
2. Preprocesses the code to match `[` and `]` into a jump table.
3. Executes instructions one by one using a tape of integers.

## 🚀 Usage

To run a Brainfuck program, import the `brain_comp` function and pass your Brainfuck code as a string:

```python
from brainfuck_interpreter import brain_comp

code = "++++++++[>++++++++<-]>+.+.+."  # Sample Brainfuck code
brain_comp(code)
```

Or, you can extend this interpreter to read from `.b` files or accept command-line input.

## 🧪 Example

### Hello World (Brainfuck)

```brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
```

Output:
```
Hello World!
```

## ⚠️ Errors

- `SyntaxError`: Raised for unmatched brackets (`[` or `]`).
- `IndexError`: Raised if the pointer moves to a negative index.

## 📄 License

This code is open source and free to use for educational purposes.
