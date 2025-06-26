# Hackaton

## Requirements
- Python 3.9

## How to Run

```
Be sure that the video named input_video.mp4 is on the root of the folder
```

First, you must create a virtual environment by running the following command:

```bash
py -m venv venv
```

> **Note**: You may need to call Python as `py` or `python` depending on your system.

To activate the virtual environment, use the following command:

```bash
source venv/bin/activate
```

If you're on Windows, use this command instead:

```bash
venv\Scripts\activate
```

Next, install the required packages by running:

```bash
pip install -r requirements.txt
```

Finally, you can run the application with the following command:

```bash
streamlit app.py
```