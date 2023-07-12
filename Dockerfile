FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r req.txt
EXPOSE $PORT
CMD ["streamlit", "run", "app.py"]
