# Projects within this repo
## react-frontend-flask-backend
### Overview

To have a front-end in `react-frontend` and backend in `flask-backend`.

In flask-backend, the sqlite database is created in the instance directory set by the Flask object's instance path. In `__init__.py`, is is the line that is `os.makedirs(app.instance_path)`. the sqlite database is initialised by a cli command, which is run when `create_app()` function is run.

### Communication between frontend and backend
The tricky bit is to handle CORS (ie webpack-dev-app running React.JS on :3000 communicating with flask app on :5000), where there are two parts.
1. Pre-flight request. This is an OPTIONS request type. The backend lets the browser know that the backend is OK with traffic from another site, by appending headers. [Note: In production, the backend should check that the frontend is from within the trusted network, before appending these headers.]
2. Actual request. This is a POST request type. In this situation, the frontend sends over a JSON object that the backend parses, and creates a row within the sqlite database. Then, the backend returns a 'Success' response. This response will likewise have to have the actual headers.

(1) and (2) are handled by the funcs `build_preflight_response()` and `build_actual_response()` respectively.
