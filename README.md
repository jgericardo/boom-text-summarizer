# Text Summarizer App

A text summarizer application built using Streamlit.

For this application, we use a small variant of BART for text summarization called [DistilBART (sshleifer/distilbart-cnn-12-6)](https://huggingface.co/sshleifer/distilbart-cnn-12-6).

## Setup

- Python version: `Python 3.11.4`
- Virtual environment (pyenv): `pyenv 2.3.25`
- Poetry: `1.6.1`
- Docker: `24.0.5`

If you have PyEnv installed, you may create a virtual environment from the project repo,

```shell
$ pyenv virtualenv 3.11.4 "<your-venv-name>"
$ pyenv local "<your-venv-name>"
```

To install dependencies using Poetry,

```shell
$ poetry install
```

To download the model files locally,

```shell
$ python modules/download_model.py
```

## Build

To create the Docker app,

```shell
$ sudo docker build . -t text-summarizer-app
```

## Usage

To run the Docker app,

```shell
$ docker run -p 8000:8000 text-summarizer-app
```

Open the local URL ("Network URL") displayed on the terminal in a browser to view the Streamlit app.
