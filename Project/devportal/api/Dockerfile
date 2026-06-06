FROM python:3.12-slim AS builder

WORKDIR /install

COPY requirements.txt .

RUN pip install --prefix=/deps --no-cache-dir -r requirements.txt


FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /deps /usr/local

COPY app.py .

RUN mkdir -p /app/logs

ENV APP_ENV=development \
    PORT=5000

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

EXPOSE 5000

CMD ["python", "app.py"]
