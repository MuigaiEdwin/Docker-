# Docker Guide: `ADD` vs `COPY` — Copying Files into Images

> **Platform:** KillerCoda | **Topic:** Dockerfile Instructions  
> **Reference:** [Docker Docs — ADD or COPY](https://docs.docker.com/develop/develop-images/instructions/#add-or-copy)

---

## Overview

Both `ADD` and `COPY` can copy files from your local machine into a Docker image during the build process. However, **`COPY` is the recommended instruction** for straightforward file copying because it is explicit and predictable. `ADD` has extra capabilities (like auto-extracting `.tar` archives and fetching remote URLs) that can lead to unexpected behaviour if you're just copying files.

> **Rule of thumb:** Use `COPY` unless you specifically need `ADD`'s extra features.

---

## What You'll Learn

- The difference between `COPY` and `ADD`
- How to modify a `Dockerfile` to copy files into an image
- How to build a Docker image and verify files were copied correctly

---

## Prerequisites

- Docker installed and running
- A working directory containing:
  - `Dockerfile`
  - `copy_file.txt`
  - `add_file.txt`

---

## Step-by-Step

### 1. Modify the Dockerfile

Open `/root/Dockerfile` and add the following lines:

```dockerfile
# Recommended: use COPY for straightforward file copying
COPY copy_file.txt /app

# ADD can also copy files, but has extra (sometimes surprising) features
ADD add_file.txt /app
```

Your `Dockerfile` should now look something like this:

```dockerfile
FROM ubuntu:latest

# Copy files into the /app directory inside the image
COPY copy_file.txt /app
ADD  add_file.txt  /app
```

---

### 2. Build the Image

Run the following command from the directory containing your `Dockerfile`:

```bash
docker build -t app-image .
```

**What this does:**
- `docker build` — triggers the image build
- `-t app-image` — tags (names) the image as `app-image`
- `.` — tells Docker to look for the `Dockerfile` in the current directory

---

### 3. Verify the Files Were Copied

Run a temporary container from the image and list the contents of `/app`:

```bash
docker run --rm app-image ls /app
```

**Expected output:**

```
add_file.txt
copy_file.txt
```

**Flags explained:**
- `--rm` — automatically removes the container after it exits (keeps things clean)
- `app-image` — the image to run
- `ls /app` — the command to execute inside the container

---

## Key Differences: `COPY` vs `ADD`

| Feature | `COPY` | `ADD` |
|---|---|---|
| Copy local files | ✅ Yes | ✅ Yes |
| Auto-extract `.tar` archives | ❌ No | ✅ Yes |
| Fetch files from a URL | ❌ No | ✅ Yes |
| Recommended for simple copies | ✅ **Preferred** | ⚠️ Not recommended |

---

## Summary

```dockerfile
COPY copy_file.txt /app   # Simple, explicit — use this for copying files
ADD  add_file.txt  /app   # Works, but best reserved for tar extraction or URLs
```

When in doubt, **use `COPY`**. It makes your intent clear and your Dockerfile easier to maintain.

---

## Quick Reference Commands

```bash
# Build the image
docker build -t app-image .

# Verify files inside the container
docker run --rm app-image ls /app

# Get help on docker build flags
docker build -h
```

---

*Part of a Docker learning series documented while working through KillerCoda labs.*