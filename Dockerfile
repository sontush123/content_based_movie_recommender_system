FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirement.txt
EXPOSE $PORT
CMD ["streamlit", "run", "app.py"]