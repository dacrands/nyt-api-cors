# New York Times API

Backend for my React/Redux application featuring the New York Times API.

| Features            | Description                   |
|---------------------|--------------------|
|GET /api/popular     |most emailed articles
|GET /api/best | New York Times best-sellers
|GET /api/archives/\<month\>/\<year\> | articles from the specified year and month 


## Table of Contents
- [Description](#description)
  - [Prerequisites](#prerequisites)
  - [Configuration](#configuration)
- [How it works](#how)
- [Hosting](#hosting)

## Description
I built this application to remove the NYT API-key from my front-end application &mdash; here is a [blog post](https://dacrands.github.io/10-7-18) I wrote on how to build such an application.    

There are three routes, each delivers an array of objects. I host this application on a *Digital Ocean* droplet &mdash; here is the [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04) I used. Additionally, this application implements CORS. 

### Prerequisites
- [Flask](http://flask.pocoo.org/) 
- cloud hosting knowledge (You can reference the blog post linked above for a start.)
- [NYT API](https://developer.nytimes.com/) key

### Configuration
You will only need to configure your API-key.

## How it Works

### CORS
The whole idea of creating this application is to protect API-keys. That said, if we don't implement CORS anyone can access the data from this API, and that isn't much better.

This application is not using cookies or any authentication whatsoever, so configuring CORS is quite simple:

```python

from flask_cors import CORS
...
CORS(app, origins="http://localhost:8880")
```

If you're not familiar with CORS, then you may not recognize that this the configuration for development. For production you would replace the origins arg with the URL for the front-end application.
