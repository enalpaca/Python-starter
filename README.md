## How to develop with VSCode?
```js
# .vscode/settings.json
{
//   "python.formatting.provider": "autopep8",
  // "python.formatting.autopep8Args": ["--ignore", "E402"],
  "terminal.integrated.env.linux": {
    "PYTHONPATH": "${workspaceFolder}/src:${env:PYTHONPATH}"
  },
  "terminal.integrated.env.osx": {
    "PYTHONPATH": "${workspaceFolder}/src:${env:PYTHONPATH}"
  },
  "terminal.integrated.env.windows": {
    "PYTHONPATH": "${workspaceFolder}/src;${env:PYTHONPATH}"
  },
}
```
#### Create venv
https://code.visualstudio.com/docs/python/environments
```bash
# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv

# Windows
python -m venv .venv
# You can also use py -3 -m venv .venv

#active venv
.venv\scripts\activate

```
#### Select interpreter
In VScode Status Bar,  select interpreter to <span style="color:red">{root folder}/.venv/Scripts/python.exe</span>

```bash
# installs packages

# macOS
python3 -m pip install matplotlib

# Windows (may require elevation)
python -m pip install matplotlib

# Linux (Debian)
apt-get install python3-tk
python3 -m pip install matplotlib
```

```bash
# installs packages
pipenv sync
# update packages
pipenv update
# update specific package
pipenv update pandas



## install packages
pip install -r requirements.txt -v

## export packages
pip freeze > requirements.txt