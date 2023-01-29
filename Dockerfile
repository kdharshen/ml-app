FROM python:3.11.1-slim
COPY requirements.txt .
RUN pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt -vvv
COPY . .
EXPOSE 1234
CMD [ "flask", "run", "--port=1234" ]
