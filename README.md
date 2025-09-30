
# DockerArchWorkshop

## Overview

This project demonstrates a simple distributed architecture using Docker Compose. It consists of a monitoring dashboard (Flask web app) and three worker nodes that communicate with the dashboard. Each node simulates a process and reports its status to the dashboard after a configurable delay.

## Architecture

```
┌────────────┐      ┌────────────┐
│  nodo_1    │      │  nodo_2    │      │  nodo_3    │
│ (worker)   │      │ (worker)   │      │ (worker)   │
└─────┬──────┘      └─────┬──────┘      └─────┬──────┘
			│                   │                   │
			└────────────┬──────┴──────┬────────────┘
									 │             │
							┌────▼─────────────▼─────┐
							│      dashboard        │
							│   (Flask web app)     │
							└───────────────────────┘
```

## Components

- **dashboard**: Flask app that displays the status of all nodes and provides an API for workers to report their status.
- **nodo_1, nodo_2, nodo_3**: Worker containers that wait for a specified time, then notify the dashboard of their activation.

## How to Run

1. Clone this repository and navigate to the project directory:
	 ```sh
	 git clone https://github.com/RoBorregos/DockerArchWorkshop.git
	 cd DockerArchWorkshop
	 ```
2. Build and start all services:
	 ```sh
	 docker-compose up --build
	 ```
3. Open your browser and go to [http://localhost:5000](http://localhost:5000) to view the dashboard.

## Customization

You can adjust the activation delay and node names in `docker-compose.yaml` under each worker's `environment` section:

```yaml
environment:
	NAME: "nodo_1"
	TIME: "10"
```

## File Structure

- `app.py` — Flask dashboard application
- `docker-compose.yaml` — Multi-container orchestration
- `Dockerfile` — Dashboard build instructions
- `workers/` — Worker node code and Dockerfile
	- `request.py` — Worker script
	- `Dockerfile` — Worker build instructions
	- `requirements.txt` — Worker dependencies
- `templates/index.html` — Dashboard UI

## How It Works

1. The dashboard starts and listens on port 5000.
2. Each worker node starts, waits for its configured time, then sends a request to the dashboard to mark itself as online.
3. The dashboard updates the UI to reflect the status of each node.

## Example Worker Command

```
python3 request.py <sleep_seconds> <node_value>
```
These arguments are set via environment variables in Docker Compose.

## License

This project is licensed under the MIT License.