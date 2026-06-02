# Docker Guide: `ADD` Remote Files vs `COPY` Local Files

> **Platform:** KillerCoda | **Topic:** Dockerfile Best Practices  
> **Reference:**
> - [Docker Docs — ADD](https://docs.docker.com/engine/reference/builder/#add)
> - [Docker Docs — COPY](https://docs.docker.com/engine/reference/builder/#copy)

---

## Overview

This lesson builds on the basics of `ADD` vs `COPY` and focuses on their **correct use cases**:

| Instruction | Best Used For |
|---|---|
| `COPY` | Copying **local** files/directories into the image |
| `ADD` | Fetching **remote** files (URLs, Git repos) into the image |

> **Why use `ADD` instead of `RUN wget`?**  
> `ADD` ensures a more precise build cache, has built-in checksum validation for remote resources, and supports parsing branches, tags, and subdirectories from Git URLs.

---

## What You'll Learn

- How to use `ADD` to fetch a remote Git repository into an image
- How to use `COPY` to copy a local file into an image
- How to build and verify the image

---

## Step-by-Step

### 1. Modify the Dockerfile

Open `/root/Dockerfile` and update it to follow best practices:

```dockerfile
# Fetch a remote Git repo using ADD (best practice over RUN wget)
ADD https://github.com/moby/buildkit.git#v0.10.1 /app

# Copy a local file using COPY
COPY add_file.txt /app
```

> **Note:** `#v0.10.1` specifies a Git tag — this pins the version for a reliable, reproducible build.

---

### 2. Build the Image

```bash
docker build -t app-image-2 .
```

**What this does:**
- `-t app-image-2` — names the new image `app-image-2`
- `.` — uses the `Dockerfile` in the current directory

---

### 3. Verify Files Were Transferred

```bash
docker run --rm app-image-2 ls /app
```

**Expected output** — you should see the cloned repo contents plus your local file:

```
add_file.txt
... (buildkit repo files)
```

---

## Key Takeaways

- **Use `COPY`** for local files — it is explicit, simple, and predictable
- **Use `ADD`** when you need to pull from a remote URL or Git repository
- **Never use `RUN wget/curl`** just to download a file — `ADD` handles it better with caching and checksum support
- Always **pin a version/tag** when using `ADD` with a Git URL (e.g. `#v0.10.1`) to keep builds reproducible

---

## Dockerfile Summary

```dockerfile
# Remote resource — use ADD
ADD https://github.com/moby/buildkit.git#v0.10.1 /app

# Local file — use COPY
COPY add_file.txt /app
```

---

## Quick Reference Commands

```bash
# Build the image
docker build -t app-image-2 .

# Verify files inside the container
docker run --rm app-image-2 ls /app
```

---

*Part of a Docker learning series documented while working through KillerCoda labs.*