# InfiniteBaseCalc

InfiniteBaseCalc is a versatile Python program that allows for the conversion of numbers from any base to any other base. It supports bases that include both fractions and negative numbers, covering a wide range of possibilities. Additionally, it features a calculator capable of evaluating expressions in any specified base.

## Features

- **Base Conversion**: Convert numbers between any bases, including fractional and negative bases, with the exception of base 0 and base 1.
- **Base Range**: Currently supports bases from -402 to 402. Users can extend this range by adding their own symbols.
- **Accuracy**: Tested for various combinations of fractional and negative bases with a detailed error rate analysis.

## Conversion Accuracy

The program has been tested extensively. The table below summarizes the error rates for different scenarios:

| Fractional Base | Negative Base | Fractional Number | Negative Number | Error Rate |
|-----------------|---------------|-------------------|-----------------|------------|
| No              | No            | No                | No              | 0%         |
| No              | No            | No                | Yes             | 0%         |
| No              | No            | Yes               | No              | 0%         |
| No              | No            | Yes               | Yes             | 0%         |
| No              | Yes           | No                | No              | 0%         |
| No              | Yes           | No                | Yes             | 0%         |
| No              | Yes           | Yes               | No              | 0%         |
| No              | Yes           | Yes               | Yes             | 0%         |
| Yes             | No            | No                | No              | 0%         |
| Yes             | No            | No                | Yes             | 0%         |
| Yes             | No            | Yes               | No              | 0.01714%   |
| Yes             | No            | Yes               | Yes             | 0.21429%   |
| Yes             | Yes           | No                | No              | 0.21429%   |
| Yes             | Yes           | No                | Yes             | 0.28667%   |
| Yes             | Yes           | Yes               | No              | 0.20707%   |
| Yes             | Yes           | Yes               | Yes             | 2.0%       |

Errors primarily occur in cases involving small fractional bases and large numbers, especially when the base is negative, due to the difficulty in accurately representing all digits.

## Calculator

InfiniteBaseCalc also includes a powerful calculator that can evaluate any expression in any specified base, enhancing its utility beyond simple number conversion.

## Files

- **logic.py**: Contains all the mathematical logic for conversions and calculations. No external libraries are used except for the built-in math library.
- **interface.py**: Uses Tkinter to provide a simple graphical user interface that includes both the converter and the calculator.
- **test.py**: Script for evaluating error rates as detailed in the accuracy table.

## Installation and Usage

Clone the repository:
```sh
git clone https://github.com/murtadha203/InfiniteBaseCalc.git
cd InfiniteBaseCalc
```
Install dependencies (only Tkinter is needed for the interface):

```sh
pip install tk
```

Run the program:
```sh
python interface.py
```

## Contributing
Contributions are welcome! If you have ideas for improvement or additional features, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.
