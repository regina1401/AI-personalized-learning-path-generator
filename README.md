# AI Personalized Learning Path Generator

An AI-based Personalized Learning Assistant built using Python and Streamlit with an interactive chatbot interface. The project provides personalized academic support, weak subject tracking, and subject-based learning assistance using Groq API and Llama models.

## Features

* Interactive AI chatbot
* Personalized learning support
* Dynamic subject management
* Weak subject tracking
* Session-based chat memory
* Simple and user-friendly UI

## Technologies Used

* Python
* Streamlit
* Groq API
* Llama 3.1 Model
* Prompt Engineering
* dotenv (.env)

## Project Structure

```bash
project/
│
├── app.py
├── chatbot.py
├── prompts.py
├── .env
└── requirements.txt
```

## Installation

1. Clone the repository

```bash
git clone <your-github-repo-link>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Add your API key inside `.env`

```env
GROQ_API_KEY=your_api_key_here
```

4. Run the application

```bash
streamlit run app.py
```

## Future Improvements

* AI-generated study planner
* Adaptive quiz generation
* RAG-based notes support
* Progress analytics dashboard



