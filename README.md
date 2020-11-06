
## Setup

From: https://anbasile.github.io/programming/2017/06/25/jupyter-venv/

```bash
$ python -m venv venv
$ . venv/bin/activate
$ pip install ipykernel
# until metomi-isodatetime with 3.8 requirement is released
$ pip install -r requirements.txt --ignore-requires-python
$ ipython kernel install --user --name=kinow-notebooks
Installed kernelspec kinow-notebooks in /home/kinow/.local/share/jupyter/kernels/kinow-notebooks
```

## Sharing

Instead of sharing a link to GitHub like https://github.com/kinow/notebooks/blob/master/python/ipython/ipython autoreload.ipynb,
it is preferable to share a link with [`nbviewer`](https://nbviewer.jupyter.org/), as GitHub does not render large notebooks.

The link above would become: https://nbviewer.jupyter.org/url/github.com/kinow/notebooks/blob/master/python/ipython/ipython%20autoreload.ipynb,
i.e. just add https://nbviewer.jupyter.org/url/ followed by the GitHub notebook URL.

