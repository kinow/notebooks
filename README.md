
## Set up

From: https://anbasile.github.io/programming/2017/06/25/jupyter-venv/

```bash
$ virtualenv venv
$ . venv/bin/activate
$ pip install ipykernel
# until metomi-isodatetime with 3.8 requirement is released
$ pip install -r requirements.txt --ignore-requires-python
$ ipython kernel install --user --name=kinow-notebooks
Installed kernelspec kinow-notebooks in /home/kinow/.local/share/jupyter/kernels/kinow-notebooks
```
