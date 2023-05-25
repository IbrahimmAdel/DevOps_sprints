FROM python:3.8
RUN pip install Flask==0.10.1 & jinja2
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]
