## Sentiment analysis tool

A web tool to evaluate sentiment analysis on a given text

### Install dependencies

```
pip install -r requirements.txt
```


### Run the app

```
py app.py
```

### Test the endpoint

```bash
curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d '{"text": "AI is amazing!"}'
```
