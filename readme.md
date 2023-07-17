# Plotter

Plotter is an app used to plot any user inputted equation between given boundaries
## images
![alt text](https://github.com/therealX01D/MicroMasterTasks/blob/main/Screenshot%202023-07-17%20232458.png)
![alttext](https://github.com/therealX01D/MicroMasterTasks/blob/main/Screenshot%202023-07-17%20233007.png)
![alt text](https://github.com/therealX01D/MicroMasterTasks/blob/main/Screenshot%202023-07-17%20235648.png)
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pyside6 matplotlib
```

## Usage

```python
python3 main.py
```
## Description
I have developed this program as a task from micromaster to apply for an internship ,in this program I have used pyside and matplotlib to plot any expression given by user in matplotlib I also used ll1 grammer to find where user had made a mistake and make a feedback to him
## ll1 grammar
E -> T E'
E' -> + T E' | - T E' | ε
T -> F T'
T' -> * F T' | / F T' | ^ F T' | ε
F -> x | number | - x | - number | ( E )
## Parse table
|   | x      | number | + T E' | - T E' | * F T' | / F T' | ^ F T' | ( E )  | )      | $      |
|---|--------|--------|--------|--------|--------|--------|--------|--------|--------|-------|
| E | T E'   | T E'   |        |        |        |        |        | T E'   |        |       |
| E'|        |        | + T E' | - T E' |        |        |        |        | ε      | ε     |
| T | F T'   | F T'   |        |        |        |        |        | F T'   |        |       |
| T'|        |        | ε      | ε      | * F T'| / F T'| ^ F T'|        | ε      | ε     |
| F | x      | number |        | - F    |        |        |        | ( E )  |        | - F   |
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## limits 
 when building the grammar i wasnt able to incoporate all case so -ve s can't appear at the beginning
 and floats cannot be presented
## License

[MIT](https://choosealicense.com/licenses/mit/)
