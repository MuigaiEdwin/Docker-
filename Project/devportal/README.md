# devportal

A two-service containerized project built to practice advanced Docker concepts. There's a Python/Flask API that returns live system info and an Nginx dashboard that talks to it — all wired together with Docker Compose.
 
This project picks up where single-container practice left off.How real applications work in Docker: multiple services, a shared network, data that survives restarts, and containers that wait for each other before starting.

---

## What I've learnt: 

- Multi-stage Docker builds and why they matter for image size
- How containers on the same network find each other by name
- Health checks — letting Docker know when a service is actually ready
- Named volumes for data that persists across container restarts
- Environment variables as the clean way to configure containers
- Docker Compose as the tool that ties everything together

---

## Project structure

```
devportal/
├── docker-compose.yml
├── api/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── dashboard/
    ├── Dockerfile
    └── index.html
```

![architechture](./architechture.png)
---

## How it works

The two services live on a private Docker network called `devnet`. Because they share that network, the dashboard can reach the API by just typing `http://api:5000` — Docker handles the DNS lookup internally. Your browser on the host machine only ever talks to the dashboard, which is the only service with an exposed port.

```
Your browser → localhost:8080 → dashboard container → api container (port 5000)
```

The API also writes to a named volume (`api-logs`) so anything it logs survives even if you tear the container down and bring it back up.

---

## Prerequisites

- Docker Desktop (or Docker Engine + Compose plugin on Linux)
- That's it — no Python or Nginx needed on your machine

---

## Running the project

Clone the repo and start everything with one command:

```bash
git clone https://github.com/muigaiedwin/devportal.git
cd devportal
docker compose up --build
```

The `--build` flag makes sure Docker rebuilds both images from scratch. You'll see both services start in the terminal — the dashboard will wait until the API passes its health check before it comes up.

Once everything is running, open `http://localhost:8080` in your browser and press the button.

To run it in the background instead:

```bash
docker compose up --build -d
```

---

## Stopping and cleaning up

Stop everything and remove the containers and network:

```bash
docker compose down
```

If you also want to delete the log volume (the persisted data):

```bash
docker compose down -v
```

To remove the built images too:

```bash
docker rmi devportal-api devportal-dashboard
```

---

## Things worth exploring

**Override environment variables at runtime**

The API reads `APP_ENV` and `PORT` from its environment. You can override them without touching the image:

```bash
docker run --rm -e APP_ENV=staging -e PORT=5001 -p 5001:5001 devportal-api
```

Then hit `http://localhost:5001/info` and you'll see `"env": "staging"` in the response.

**Inspect the Docker network**

```bash
docker network ls
docker network inspect devportal_devnet
```

This shows you both containers, their internal IP addresses, and how Docker connected them.

**Inspect the volume**

```bash
docker volume ls
docker volume inspect devportal_api-logs
```

The `Mountpoint` field tells you exactly where Docker is storing the data on your machine.

**Check container health**

```bash
docker ps
```

Look at the `STATUS` column. The API will show `(healthy)` once it passes its first health check. If something breaks, it shows `(unhealthy)` — no need to exec into the container to know something is wrong.

**Scale the API**

First remove the `container_name: api` line from `docker-compose.yml` (static names block scaling), then:

```bash
docker compose up --scale api=3 -d
```

This spins up three replicas of the API service.

---

## Concepts explained

### Multi-stage builds

The API Dockerfile has two `FROM` statements. The first stage (called `builder`) installs all the Python dependencies. The second stage copies only the installed packages from that first stage and discards everything else — no pip cache, no build tools, no temp files. The result is a noticeably smaller final image.

### Health checks

The `HEALTHCHECK` instruction in the Dockerfile tells Docker to periodically run a command against the running container. If it fails three times in a row, Docker marks the container as `unhealthy`. Compose uses this status with `depends_on: condition: service_healthy` to hold the dashboard back until the API is genuinely ready — not just started, but actually responding.

### Named volumes

A named volume like `api-logs` is managed by Docker, not tied to a specific path on your machine. The data inside it survives `docker compose down`. You have to explicitly pass `-v` to delete it. This is how you'd handle a database in a containerized setup.

### Docker networking and DNS

When you put two services on the same Compose network, Docker registers each container's name as a DNS hostname on that network. So `http://api:5000` works inside the dashboard container the same way `http://google.com` works in your browser — Docker resolves the name `api` to the right internal IP automatically.

---
