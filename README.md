## Sentiment analysis tool

A web tool and API to evaluate sentiment analysis on a given text

### Demo

You can try the app in [streamlit](https://mood-check-6tfngybm8jfffwvgtxoo6d.streamlit.app/)


### Install dependencies

```
pip install -r requirements.txt
```

### Run the API

```bash
python api.py
```

**Test the endpoint**

```bash
curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d '{"text": "AI is amazing!"}'
```

### Run the app locally using streamlit

```bash
streamlit run app.py
``` 
