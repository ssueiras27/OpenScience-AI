FROM python:3.10.10-bullseye

RUN python3 -m venv venv

# Install dependencies:
COPY requirements.txt .
RUN . venv/bin/activate && pip install -r requirements.txt

# Run the application:
COPY /pdfanalyzer/main.py .
CMD . venv/bin/activate && exec python ./pdfanalyzer/main.py