FROM python:3.11.3
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p ./google/bert-base-local-results
RUN wget -O ./google/bert-base-local-results/.gitattributes https://huggingface.co/serpapi/bert-base-local-results/resolve/main/.gitattributes
RUN wget -O ./google/bert-base-local-results/README.md https://huggingface.co/serpapi/bert-base-local-results/resolve/main/README.md
RUN wget -O ./google/bert-base-local-results/pytorch_model.bin https://huggingface.co/serpapi/bert-base-local-results/resolve/main/pytorch_model.bin
RUN wget -O ./google/bert-base-local-results/special_tokens_map.json https://huggingface.co/serpapi/bert-base-local-results/resolve/main/special_tokens_map.json
RUN wget -O ./google/bert-base-local-results/tokenizer_config.json https://huggingface.co/serpapi/bert-base-local-results/resolve/main/tokenizer_config.json
RUN wget -O ./google/bert-base-local-results/vocab.txt https://huggingface.co/serpapi/bert-base-local-results/resolve/main/vocab.txt
RUN wget -O ./google/bert-base-local-results/config.json https://huggingface.co/serpapi/bert-base-local-results/resolve/main/config.json
COPY . .
CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0"]
