# ITerative Metrics

Create a cumulative flow diagram for our team metrics.

## Usage Guide

The software requires python3. You need some basic python programming experience to use the software.

### Install dependencies

```shell
pip install -r requirements.txt
```

### Render Cumulative Flow Diagram

```shell
python main.py
```

If you run the script from the command line, then a window showing the diagram will open. Press `q` to close the window.

If you run the `main.py` file from JetBrains PyCharm with **Scientific Mode** enabled in the **View** menu, then you can copy-paste the diagram.

### Add data

- Edit the file [cumulative_flow_diagram.py](src/iterative_metrics/cumulative_flow_diagram.py)
- Append a row with the next date to the variable `dates`
- Append the data from the board to every array in the `metrics` map
- Save the file
- Run `main.py` to update the diagram
- Make a commit

## Development Guide

### Run the tests

```shell
python -m pytest
```

### Build package

```shell
python -m build
```
