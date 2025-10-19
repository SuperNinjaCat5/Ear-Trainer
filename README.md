# 🎵🎶🎺🎷🎻 Ear Trainer

SOM project to help me improve at music, coding, and web design.

Demo: [music.superninjacat5.us](https://music.SuperNinjaCat5.us)

## About the project
- Simple, fun project to help me improve my ear for jazz band 🎷🎷🎷🎷🎷🎷🎷
- Created by your's truly: SuperNinjaCat5

## Current features
- Two modes:  
  1. Quiz mode  
  2. Learn mode  
- Terminal-based version (i guess windows only L)
- No global variables (supports multiple users I THINK)  

## Setup
1. Git clone
2. Create leadboard.json, add {"Ilovepi3141": {"scores": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}}
3. Install stuff: ```bash pip install Flask flask-dance python-dotenv
4. Create a github oauth
5. Create a .env with FLASK_SECRET_KEY, GITHUB_OAUTH_CLIENT_ID, GITHUB_OAUTH_CLIENT_SECRET.
6. Make sure it works locally
7. Server it

---
🎵🎶🎺🎷🎻

## Deploying with Coolify

This project includes a Dockerfile configured to run Gunicorn on port 3000 which is what Coolify will use to deploy the app.

What to set in Coolify:
- Build: use the included `Dockerfile` (no custom build command required)
- Environment variables: `FLASK_SECRET_KEY`, `GITHUB_OAUTH_CLIENT_ID`, `GITHUB_OAUTH_CLIENT_SECRET`
- Exposed port: `3000`

If you can't run Gunicorn on Windows, use WSL for local testing or use the provided `start.sh` script on Linux containers.


