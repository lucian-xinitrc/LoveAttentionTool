# Love Attention Tool

## $ intro
This is a small Python-based project that activates a simple raspberry pi christmas tree's light when it receives an GET or POST request with text "start".

I have made this project so my girlfriend can activate the tree's lights when she needs attention from me.

## $ usage
Running main.py and sending POST or GET request with dict index "message" and value "start"

### Example
```
curl -X POST https://formylove.ngrok.dev/start-tree \
     -H "Content-Type: application/json" \
     -d '{"message": "start"}'
```

## $ languages used
The project was built using the following technologies:

![Python, Flask, Vim](https://skillicons.dev/icons?i=python,flask,vim)

## $ license
This project uses tree library from [ThePiHut](https://github.com/ThePiHut/rgbxmastree) 

This project is for personal use and learning purposes. Feel free to explore and modify it as needed. ❤️
