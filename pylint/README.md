# Usage
```
wget https://raw.githubusercontent.com/strg2/templates/main/pylint/pylintrc
wget https://google.github.io/styleguide/pylintrc

# single file
pylint --rcfile=pylintrc --exit-zero script.py

# directory
pylint --rcfile=pylintrc --exit-zero /path/to/dir

```
Option ``--exit-zero`` makes pylint not fail CI runs.

## rcfile
https://google.github.io/styleguide/pyguide.html<br>
https://google.github.io/styleguide/pylintrc

Has ``indent-string`` with 2 indentation blanks at last access. File in this repo has 4 blanks.

# Installation
```
python -m pip install pylint --upgrade
```
