# Docker Guide: Using CMD

> **Platform:** KillerCoda | **Topic:** CMD & ENTRYPOINT  
> **Reference:** [Docker Docs — CMD](https://docs.docker.com/engine/reference/builder/#cmd)

---

## Overview

`CMD` provides the default command that runs when a container starts. It can be **overridden at runtime** via the CLI without modifying the Dockerfile.

> Only the **last `CMD`** in a Dockerfile takes effect if there are multiple.

---

## Step-by-Step

### 1. Build the image

```bash
docker build -t cmd-echo .
```

### 2. Inspect the CMD

```bash
docker inspect cmd-echo | jq .[0].Config.Cmd
```

### 3. Run with default CMD

```bash
docker run --rm cmd-echo
```

### 4. Override CMD at runtime

```bash
docker run --rm cmd-echo date
```

Anything after the image name **replaces** the CMD defined in the Dockerfile.

### 5. Set ENTRYPOINT via CLI

```bash
docker run --rm --entrypoint date cmd-echo
```

---

## CMD vs ENTRYPOINT at a glance

| | `CMD` | `ENTRYPOINT` |
|---|---|---|
| Overridable at runtime | ✅ Yes | ⚠️ Only with `--entrypoint` |
| Purpose | Default command/args | Fixed executable |

---

## Quick Reference

```bash
docker build -t cmd-echo .                    # build image
docker inspect cmd-echo | jq .[0].Config.Cmd  # check CMD
docker run --rm cmd-echo                      # default CMD
docker run --rm cmd-echo date                 # override CMD
docker run --rm --entrypoint date cmd-echo    # set ENTRYPOINT via CLI
```

---

*Part of a Docker learning series documented while working through KillerCoda labs.*