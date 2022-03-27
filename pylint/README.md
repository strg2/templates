# Usage
https://pylint.pycqa.org/en/latest/user_guide/run.html
```
# single file
pylint --rcfile=pylintrc --exit-zero script.py

#directory containing __init__.py
pylint --rcfile=pylintrc --exit-zero -recursive=y /path/to/dir

```
Option ``--exit-zero`` makes pylint not fail CI runs.

## rcfile
https://google.github.io/styleguide/pyguide.html
https://google.github.io/styleguide/pylintrc

Has ``indent-string`` with 2 indentation blanks at last access. File in this repo has 4 blanks.

# Installation
```
pip install pylint  --upgrade
```
