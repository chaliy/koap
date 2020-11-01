FROM python:3.9-slim

RUN mkdir -p /app && \
    addgroup --quiet --system --gid 1000 app && \
    adduser --quiet --system --home /app --uid 1000 --group app --disabled-password  && \
    chown -R app:app /app
WORKDIR /app
RUN pip install --no-cache-dir pipenv

# Install Pipfile dependencies
COPY --chown=app:app koap/Pipfile* /app/
RUN pipenv install --deploy --system

COPY --chown=app:app koap/*.py /app/
COPY --chown=app:app koap-ui/build/ /app/public/

USER app

ENV KOAP_STATIC_BASE '/app/public'
EXPOSE 8080

ENTRYPOINT [ "python", "main.py" ] 
