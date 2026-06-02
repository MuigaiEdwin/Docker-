# Docker Guide: Building an Image from Scratch

> **Platform:** KillerCoda | **Topic:** Dockerfile, Images & Containers

---

## Key Concepts

| Term | Meaning |
|---|---|
| `Dockerfile` | List of instructions to build an image |
| `Image` | Binary file with all data/requirements to run |
| `Container` | A running instance of an image |
| `Registry` | Place to push/pull images (e.g. Docker Hub) |

---

## Step-by-Step

### 1. Create the Dockerfile

```dockerfile
FROM bash
CMD ["ping", "killercoda.com"]
```

- `FROM bash` — uses bash as the base image
- `CMD` — default command that runs when the container starts

### 2. Build & verify the image

```bash
docker build -t pinger .
docker image ls
```

### 3. Run the container

```bash
docker run --name my-ping pinger
```

---

## Quick Reference

```bash
docker build -t pinger .        # build and tag image
docker image ls                 # list images
docker run --name my-ping pinger  # run named container
```

---

*Part of a Docker learning series documented while working through KillerCoda labs.*