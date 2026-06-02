# Docker Guide: Push Image with Custom Tag to Registry

> **Platform:** KillerCoda | **Topic:** Image Tagging & Registry

---

## Overview

Without a tag, Docker defaults to `:latest`. This lesson covers tagging an image with a custom version and pushing it to a registry.

---

## Step-by-Step

### 1. Tag the image

```bash
docker tag pinger pinger:v1
docker tag pinger local-registry:5000/pinger:v1
```

- `pinger:v1` — version tag for local use
- `local-registry:5000/pinger:v1` — tagged for a specific registry and port

### 2. Verify tags

```bash
docker image ls
```

You'll see the same image listed under multiple tags.

### 3. Push to registry

```bash
docker push local-registry:5000/pinger:v1
```

---

## Key Takeaways

- One image can have **multiple tags**
- Format for registry push: `registry-host:port/image-name:tag`
- Always tag with a version (`:v1`, `:v2`) instead of relying on `:latest` in production

---

*Part of a Docker learning series documented while working through KillerCoda labs.*