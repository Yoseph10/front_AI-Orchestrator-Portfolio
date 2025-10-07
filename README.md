# 🤖 AI Portfolio Frontend

This repository contains the **frontend application** of the Intelligent Portfolio project — an AI-driven assistant that allows recruiters, clients, and students to interact dynamically with Yoseph Ayala’s professional portfolio.

The frontend is built with **Gradio** and **FastAPI**, providing an interactive web interface that connects directly to the backend API hosted on **Google Cloud Run**.

---

## 🧠 Overview

The AI Portfolio Frontend serves as the **user interface layer**, allowing real-time chat interactions with a multi-agent backend powered by Retrieval-Augmented Generation (RAG).

### 🔗 Related Backend

The backend that processes all AI logic and responses is available here:
👉 [AI-Orchestrator-Portfolio (Backend)](https://github.com/Yoseph10/AI-Orchestrator-Portfolio)

---

## ⚙️ Tech Stack

* **Gradio** — Web interface for conversational AI
* **FastAPI** — Mounted to serve the Gradio app via HTTP
* **Python 3.10+**
* **Docker** — Containerized deployment
* **Google Cloud Run** — Serverless hosting for the frontend

---

## 📁 Project Structure

```
.
├── .dockerignore
├── .gitignore
├── Dockerfile
├── app.py
├── requirements.txt
└── .env
```

---

## 🧩 Environment Variables

Create a `.env` file in the root directory to specify your backend API endpoint:

```
API_GENAI=https://ai-portafolio-backend-xxxxxx-uc.a.run.app/chat
```

---

## 🚀 Run Locally

### 1. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate    # (On Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

### 2. Run the app locally

```bash
uvicorn app:app --reload
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 🐳 Deploy with Docker

### 1. Build the Docker image

```bash
docker build -t ai_portfolio_front .
```

### 2. Run the container locally

```bash
docker run -p 8080:8080 ai_portfolio_front
```

---

## ☁️ Deploy to Google Cloud Run

Once your Docker image is built, push it to **Artifact Registry** and deploy it to **Cloud Run**.

### 1. Tag and push the image

```bash
docker tag ai_portfolio_front us-central1-docker.pkg.dev/PROJECT_ID/REPO_NAME/ai_portfolio_front:latest
docker push us-central1-docker.pkg.dev/PROJECT_ID/REPO_NAME/ai_portfolio_front:latest
```

### 2. Deploy to Cloud Run

```bash
gcloud run deploy ai-portfolio-frontend \
  --image us-central1-docker.pkg.dev/PROJECT_ID/REPO_NAME/ai_portfolio_front:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars API_GENAI=https://ai-portafolio-backend-xxxxxx-uc.a.run.app/chat
```

---

## 💬 Features

* Elegant Gradio interface with custom styling (CSS theme)
* FastAPI integration for deployment
* Persistent conversation flow between user and assistant
* Responsive design for all device sizes
* Secure configuration through `.env` variables

---

## 📘 Notes

* The frontend communicates with the backend through the endpoint stored in `API_GENAI`.
* The backend implements a **multi-agent RAG architecture**, enabling intelligent portfolio responses, meeting scheduling, and tailored interactions.
* Both frontend and backend are independently deployed on **Google Cloud Run**, ensuring full scalability.

---

## 🧑‍💻 Author

**Yoseph Ayala**
Data Scientist | AI Engineer
📍 Peru
🔗 [LinkedIn](https://www.linkedin.com/in/yoseph-daniel-ayala-valencia-9863521b0/)
