#!/usr/bin/env bash
set -eu

uvicorn server.server:app --host 0.0.0.0 --port 8999 --workers 24
