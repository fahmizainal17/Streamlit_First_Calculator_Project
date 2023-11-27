Certainly! Here's your project documentation formatted in the style you provided:

```markdown
# My Streamlit First Project

Libraries and Packages:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Github Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

## Introduction
This documentation provides a comprehensive overview of my first Streamlit project. The project involves creating a basic calculator application using the Streamlit framework. The documentation covers the project's objectives, requirements, structure, and how to run the application.

## Project Objectives
The primary objectives of this project are to implement Git and GitHub knowledge in production, learn application deployment fundamentals, adapt to software engineering practices, understand PR and code review workflows, implement SOLID principles in design, and write well-documented code.

## Streamlit App: MyCalculator

### Task
Streamlit web application with basic calculator features.

1. The code was developed on Visual Studio
2. Calculator features:
   - Addition (adding 2 numbers)
   - Subtraction (subtracting 2 numbers)
   - Division (dividing 2 numbers)
   - Multiplication (multiplying 2 numbers)
   - Exponential (number to the power of the one)
3. Titles and necessary cosmetics were included
4. Repository structure:
   ```
   .app/
       |-- main_ui.py
       |-- calculator.py
       |-- utils.py
       |-- requirements.txt
       |-- .gitignore
   ```
5. Function or method line be within our palm size.
6. Single responsibility methodology was applied.
7. Functions have docstring and necessary comments.
8. User-friendly application.

## Streamlit Application Structure

- **main_ui.py**: Streamlit user interface code.
- **calculator.py**: Implements calculator functionality.
- **utils.py**: Contains utility functions or helper functions.
- **requirements.txt**: Lists the dependencies for the project.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## How to Run

1. Install required dependencies:
   ```
   pip install -r .app/requirements.txt
   ```

2. Navigate to `.app` directory:
   ```
   cd .app
   ```

3. Run Streamlit app:
   ```
   streamlit run main_ui.py
   ```

4. Open your web browser, go to the provided local URL to interact with the calculator.

## Documentation

### `main_ui.py`

- Streamlit user interface code.
- UI layout and appearance were customized.

### `calculator.py`

- Implements calculator functionality.
- Functions for addition, subtraction, multiplication, and division.

### `utils.py`

- Availability of Utility functions or helper functions.

### Contributing
Asides from the project I also learnt on how to contribute properly
- To contribute:
  - Fork the repository.
  - Create a new branch for your feature or bug fix.
  - Make changes and submit a pull request.

### Code Review Guidelines

- Adhere to SOLID principles.
- Keep functions or methods concise.
- Provide docstrings and necessary comments for clarity.
- Test application thoroughly before submitting a pull request.

```
