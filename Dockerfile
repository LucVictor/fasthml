FROM python:3.12
COPY ./ /
WORKDIR /
RUN ls -a
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]