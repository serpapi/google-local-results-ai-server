<h1 align="center">Google Local Results AI Server</h1>

<div align="center">

  <a href="">[![Contributors][contributors-shield]][contributors-url] </a>
  <a href="">[![Forks][forks-shield]][forks-url]</a>
  <a href="">[![Stargazers][stars-shield]][stars-url]</a>
  <a href="">[![Issues][issues-shield]][issues-url]</a>
  <a href="">[![Issues][issuesclosed-shield]][issuesclosed-url]</a>
  <a href="">[![MIT License][license-shield]][license-url]</a>
 
</div>

<p align="center">
  <img src="https://user-images.githubusercontent.com/73674035/247621175-3b738b9c-499e-43c9-a45a-49a9a1f2f7c8.png" alt="AI Model Server" width="50%"/>
</p>

This repository contains the code for a server that mimics the Inference API endpoints at Huggingface for BERT-based classification models. The server provides a simple interface to perform text classification using BERT models. It is designed by [SerpApi](https://serpapi.com/) for the heavy-load prototyping, and production tasks for the implementation of [`google-local-results-ai-parser` gem](https://github.com/serpapi/google-local-results-ai-parser) which uses [`serpapi/bert-base-local-results` model](https://huggingface.co/serpapi/bert-base-local-results).


<div align="center"><b>Relevant Sources</b></div>

- [**Google Local Results AI Parser**](https://github.com/serpapi/google-local-results-ai-parser): Ruby Gem for extracting structured data from Google Local Search Results using the `serpapi/bert-base-local-results` transformer model
- [**BERT-Based Classification Model for Google Local Listings**](https://huggingface.co/serpapi/bert-base-local-results): BERT-based classification model developed using the Hugging Face library, and a dataset gathered by SerpApi's Google Local API.
- [**BERT**](https://huggingface.co/docs/transformers/model_doc/bert): A language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
- [**SerpApi's Google Local Results API Documentation**](https://serpapi.com/google-local-api): A documentation on SerpApi's Scraper API for Google Local Search Results. The model within the repository has been created using this tool.
---
<h2 align="center">Installation</h2>

To set up and run the Google Local Results AI Server locally, follow these steps:
- **Clone the repository**:
```bash
cd google-local-results-ai-server
git clone git clone https://huggingface.co/serpapi/bert-base-local-results ./google/bert-base-local-results
```

- **Create and activate a virtual environment (optional but recommended)**:
```bash
python3 -m venv env
source env/bin/activate
```

- **Install the dependencies**:
```bash
pip install -r requirements.txt
```

- **Set the necessary environment variables at `main.py`:**
```py
# Master key to keep track of access
MASTER_KEY = "master_key"
```

- **Clone the contents of the [Huggingface Repository](https://huggingface.co/serpapi/bert-base-local-results) to `google/bert-base-local-results` folder.**
```bash
# Make sure you have git-lfs installed (https://git-lfs.com)
git lfs install
git lfs pull
git clone https://huggingface.co/serpapi/bert-base-local-results google/bert-base-local-results
```

- **Start the server using gunicorn:**
```bash
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0
```

You may set the number of workers depending on your system allowace. The server will start running on `http://localhost:8000`.

---

<h2 align="center">Docker Deployment</h2>

Alternatively, you can deploy the Google Local Results AI Server using Docker. The repository already contains a Dockerfile for easy deployment.

A Docker Image will be created and published in the repository.

To build the image, and deploy the server with Docker locally, follow these steps:
- **Set the necessary environment variables at `main.py`:**
```py
# Master key to keep track of access
MASTER_KEY = "master_key"
```

- **Build the Docker image**:
```bash
docker build -t google-local-results-ai-server .
```

- **Optional: Change the number of workers depending on your system allowance in `Dockerfile`. Here's an example with 2 workers:
  - `CMD ["gunicorn", "main:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0"]`

- **Run the Docker container**:
```bash
docker run -p 8000:8000 google-local-results-ai-server
```

The server will start running on `http://localhost:8000`.

---
<h2 align="center">Usage</h2>

The server exposes an HTTP API endpoint that accepts POST requests for classification. You can send requests to the API endpoint using various programming languages and tools. The following examples demonstrate how to make requests using Ruby, Python, JavaScript, and cURL.

<h3 align="center">Ruby Example</h3>

```ruby
require 'http'

url = "http://127.0.0.1:8000/models/serpapi/bert-base-local-results"
headers = { "Authorization" => "Bearer XXXXXX" }
payload = { "inputs" => "5540 N Lamar Blvd #12 Austin, TX 78756" }

response = HTTP.headers(headers).post(url, json: payload)
output = response.parse
```

<h3 align="center">Python Example</h3>

```py
import requests

API_URL = "http://127.0.0.1:8000/models/serpapi/bert-base-local-results"
headers = {"Authorization": "Bearer XXXXXX"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": "5540 N Lamar Blvd #12 Austin, TX 78756",
})
```

<h3 align="center">JavaScript Example</h3>

```js
async function query(data) {
    const response = await fetch(
        "http://127.0.0.1:8000/models/serpapi/bert-base-local-results",
        {
            headers: { Authorization: "Bearer XXXXXX" },
            method: "POST",
            body: JSON.stringify(data),
        }
    );
    const result = await response.json();
    return result;
}

query({"inputs": "5540 N Lamar Blvd #12 Austin, TX 78756"}).then((response) => {
    console.log(JSON.stringify(response));
});
```

<h3 align="center">cURL Example</h3>

```curl
curl http://127.0.0.1:8000/models/serpapi/bert-base-local-results \
    -X POST \
    -d '{"inputs": "5540 N Lamar Blvd #12 Austin, TX 78756"}' \
    -H "Authorization: Bearer XXXXXX"
```

<h3 align="center">Example JSON Output</h3>

```json
[
  [
    {
      "label": "address",
      "score": 0.9988067150115967
    },
    {
      "label": "type",
      "score": 0.0010613144841045141
    },
    {
      "label": "description",
      "score": 0.00021563934569712728
    },
    {
      "label": "hours",
      "score": 0.0002154999820049852
    },
    {
      "label": "phone",
      "score": 0.00018228559929411858
    },
    {
      "label": "reviews",
      "score": 0.00007934834866318852
    },
    {
      "label": "service options",
      "score": 0.0000681085730320774
    },
    {
      "label": "price",
      "score": 0.00001069890731741907
    },
    {
      "label": "years in business",
      "score": 0.000007037287559796823
    },
    {
      "label": "button text",
      "score": 0.000006214133918547304
    },
    {
      "label": "rating",
      "score": 0.000004599460226017982
    }
  ]
]
```
---
<h2 align="center">Advanced Usage</h2>

The server code provided in this repository supports advanced usage, allowing you to extend the models served by adding more BERT-based classification models. However, please note that the existing models are hardcoded with their paths in the code. The current model, `google/bert-base-local-results`, is located at `./google/bert-base-local-results`.

To add more models, follow these steps:

- Prepare the BERT-based classification model and save it in a directory.
- Update the models dictionary in the code to include the new model name and its corresponding directory path.
```py
models = {
    "serpapi/bert-base-local-results": "./google/bert-base-local-results",
    "new-repository/new-model": "new-model-folder-path"
}
```
- Restart the server.

The server will automatically load the new models at startup, and you can access them using the appropriate API endpoints.

Please note that you need to ensure the model directory contains the necessary files for the BERT-based classification model, such as the model weights, configuration, and tokenizer.


[contributors-shield]: https://img.shields.io/github/contributors/serpapi/google-local-results-ai-server.svg
[contributors-url]: https://github.com/serpapi/google-local-results-ai-server/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/serpapi/google-local-results-ai-server.svg
[forks-url]: https://github.com/serpapi/google-local-results-ai-server/network/members
[stars-shield]: https://img.shields.io/github/stars/serpapi/google-local-results-ai-server.svg
[stars-url]: https://github.com/serpapi/google-local-results-ai-server/stargazers
[issues-shield]: https://img.shields.io/github/issues/serpapi/google-local-results-ai-server.svg
[issues-url]: https://github.com/serpapi/google-local-results-ai-server/issues
[issuesclosed-shield]: https://img.shields.io/github/issues-closed/serpapi/google-local-results-ai-server.svg
[issuesclosed-url]: https://github.com/serpapi/google-local-results-ai-server/issues?q=is%3Aissue+is%3Aclosed
[board-shield]: https://img.shields.io/badge/Kanban-Board-grey?logo=data:image/svg%2bxml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEzLjM1MiAxNC41ODVsLTQuNTA5IDQuNjE0LjcyLTQuMDYyTDMuNDI4IDcuNTcgMCA3Ljc1MyA3LjU4IDB2Mi45NTNsNy4yMTQgNi42NDYgNC41MTMtMS4xMDUtNC42ODkgNC45ODJMMjQgMjRsLTEwLjY0OC05LjQxNXoiLz48L3N2Zz4=
[board-url]: https://github.com/serpapi/google-local-results-ai-server/projects/1
[license-shield]: https://img.shields.io/github/license/serpapi/google-local-results-ai-server.svg
[license-url]: https://github.com/serpapi/google-local-results-ai-server/blob/master/LICENSE
