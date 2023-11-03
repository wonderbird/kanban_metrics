# ITerative Metrics

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This is a prototype application with the following use cases:

- Count number of work items per workflow step of our team kanban board
- Create a cumulative flow diagram for our team metrics

## Acknowledgements

Thanks to [Michael Mahlberg](https://github.com/michaelmahlberg) for giving the original idea.

Many thanks to [JetBrains](https://www.jetbrains.com/?from=malimo) who provide
an [Open Source License](https://www.jetbrains.com/community/opensource/) for this project ❤️.

## Status

This project is a learning project. At the moment I have switched my focus and the project is sleeping. You are always welcome to send a message to me, if you are interested and have questions.

The green checkmarks in the diagram [Design level event storming](./docs/04_design_level_event_storming.drawio.png) show where I have stopped.

The next step is to sort the workflow steps so that they are always row by row, from right to left. You might want to finish the consistent rules inside the "Consider team board customization" policy first (see section Design Documentation below).

## Glossary and Concepts

We consider our team being a "production system". Our "products" are represented by "work items". The "board" visualizes the status of our "production system", i.e. which work items are currently in which workflow step of the value chain?

![model.drawio.png](docs/model.drawio.png)

## Design Documentation

In the [docs](./docs) folder you can find drawings showing the application design:

- [Big picture event storming](./docs/01_big_picture_event_storming.drawio.png) depicts the overarching workflow of gathering metrics and deriving a cumulative flow diagram
- [Design level event storming](./docs/04_design_level_event_storming.drawio.png) adds details helping to design the application

The remaining diagrams have been created on the way and may add additional insights.

## Usage Guide

The software requires python3. You need some basic python programming experience to use the software.

You run the [main.py](src/iterative_metrics/main.py) script to execute the program - details are given below. If you run it from the command line, then a window showing the diagram will open. Press `q` to close the window.

If you run [main.py](src/iterative_metrics/main.py) from JetBrains PyCharm with **Scientific Mode** enabled in the **View** menu, then you can copy-paste the diagram.

### Install dependencies

```shell
pip install -r requirements.txt
```

### Install package in editable mode

```shell
pip install --editable .
```

### Count work_items on screenshot of a kanban board

- Replace the file [kanban_board.png](client-data/kanban_board.png) with a current screenshot of the kanban board

```shell
python src/iterative_metrics/main.py
```

### Render Cumulative Flow Diagram

#### Update input data

- Edit the file [cumulative_flow_diagram.py](src/iterative_metrics/adapters/inbound/cumulative_flow_diagram.py)
- Append a row with the next date to the variable `dates`
- Append the data from the board to every array in the `metrics` map
- Save the file
- Make a commit with message "feat: metrics for today"

#### Render CFD

```shell
python src/iterative_metrics/main.py
```

## Development Guide

### Run the tests

```shell
python -m pytest
```

### Build package

```shell
python -m build
```
