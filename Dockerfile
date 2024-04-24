FROM python:3.12
ENV PORT=8080
WORKDIR /app
COPY gRPC_Server/src/generated /app/src/generated
COPY Libraries/python_common /app
COPY gRPC_Stub/line /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "API.py"]