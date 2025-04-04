#!/bin/bash

litestar database upgrade --no-prompt
litestar run --host 0.0.0.0 --port 8000