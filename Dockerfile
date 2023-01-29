FROM python:3.11-alpine
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org scikit-learn -vvv
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org Flask -vvv
COPY . .
EXPOSE 1234
CMD [ "flask", "run", "--port=1234" ]
