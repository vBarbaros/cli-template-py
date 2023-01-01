Welcome to this repository for a command line interface (CLI) 
template implemented in Python!

This repository includes a template for creating a CLI in Python, with a 
minimal set of features and a simple structure that is easy to understand and modify. 
You can use this template as a starting point for building your own CLI, or as a reference
to help you understand how CLIs work in Python.

The repository includes the source code for the template CLI, as well as documentation and 
examples of how to use it. To get started, simply clone the repository and customize the 
template to suit your needs.

Whether you're a beginner looking for a simple starting point for your first CLI, or an 
experienced developer looking for a reference implementation to use as a basis for your 
own CLIs, we hope you'll find this repository useful. If you have any questions or suggestions, 
please don't hesitate to open an issue or submit a pull request.

Thank you for visiting this repository, and we hope you find it helpful!

## Examples

```
# examples of API calls invoking
$ python3 src/run.py --get 1                           
Connection Error: Please provide a valid URL

$ python3 src/run.py --put 1
Error: 404

$ python3 src/run.py --post 1
Error: 404

$ python3 src/run.py --delete 1
Error: 404


# example of IO operations invoking
$ python3 src/run.py --input input.txt --output out.txt
```

## Run unit tests
```
$ python3 -m unittest 

# expected output
RUNNING TESTS FOR ../data/ dir - input.txt
Ensure input.txt file exists
OK
.
RUNNING TESTS FOR ../scripts/ dir - out.txt
Ensure out.txt file exists
OK
.
RUNNING TESTS FOR ../scripts/ dir - api_calls.py
Ensure api_calls.py file exists
OK
.
RUNNING TESTS FOR ../scripts/ dir - io_ops.py
Ensure io_ops.py file exists
OK
.
RUNNING TESTS FOR ../src/ dir - run.py
Ensure run.py file exists
OK
.
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```