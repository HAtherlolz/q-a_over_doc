# LLM Q&A over PDF Document
## 1) Create and set variables into .env file
### .env example
```
OPENAI_API_KEY=
OPENAI_VERSION=gpt-4
```

## 2) Install dependencies using command
```commandline
pip install -r requirements.txt
```

## 3) Run the server using command
```commandline
uvicorn main:app
```

## 4) Follow the link in a browser
```commandline
http://127.0.0.1:8000/
```

## 5) Upload pdf files

## 6) Follow the link in a browser (or use the button Go to Qa Page)
```commandline
http://127.0.0.1:8000/qa/
```

## 7) Ask questions

## It also can be used the endpoints from swagger
```commandline
http://127.0.0.1:8000/api/v1/docs/
```