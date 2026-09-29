# AGENTIC_TRAVEL_PLANNER
# AI Travel Planner

A travel planning app that creates a day-by-day itinerary based on your starting location, destination, trip length, group size, budget, and preferences.

The Streamlit interface sends trip details to a FastAPI backend. The backend uses LangChain and a Groq model to generate transportation suggestions, accommodation ideas, activities, and an estimated budget breakdown.

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **AI:** LangChain, Groq (`openai/gpt-oss-20b`)
- **Language:** Python

## Features

- Personalized day-by-day itinerary
- Transportation and accommodation suggestions
- Food and activity recommendations
- Estimated trip costs and budget comparison
- Suggestions to reduce costs when a trip exceeds the budget

> Prices are AI-generated estimates. The app does not check live fares, hotel availability, or current attraction prices.

## Run Locally

You need Python and a [Groq API key](https://console.groq.com/keys).

From the project folder, install the packages:

```powershell
py -m pip install fastapi uvicorn langchain-groq streamlit requests
```

Open a terminal for the backend:

```powershell
cd be
$env:GROQ_API_KEY="YOUR_GROQ_API_KEY"
py -m uvicorn main:f_obj --reload
```

Keep that terminal open. In a **second terminal**, from the main project folder, start the frontend:

```powershell
py -m streamlit run fe\app.py
```

Open the local URL shown by Streamlit, usually `http://localhost:8501`.

## Project Structure

```text
be/
  main.py          FastAPI endpoint and travel-planning prompt
fe/
  app.py           Streamlit interface
README.md
```

The backend accepts trip details at `POST /plan_trip`. You can view its API documentation at `http://127.0.0.1:8000/docs` while it is running.

## API Key Safety

Keep your Groq API key out of `main.py` and GitHub. The backend should read it using:

```python
api_key=os.environ["GROQ_API_KEY"]
```

Set `GROQ_API_KEY` in the terminal before starting the backend.
