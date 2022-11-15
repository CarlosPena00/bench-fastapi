# Bench-FastAPI

This repository is a sandbox to simulate a server connected to an oracle database (I/O-bound) and perform a calculation (CPU-bound). Both operations were made to last approximately 1 second (at low load).

The results folder indicates the locust test output using the following:

* Server: Ryzen 5 5600x
* Locust: Intel i5-5200U

## Install

Oracle Server
> docker run -d -p 1521:1521 -e ORACLE_PASSWORD=chcp \
  -v oracle-volume:/opt/oracle/oradata gvenzl/oracle-xe

Python

```py
conda env create
```

## Run

### Server (Python)
```py
conda activate bench
sh scripts/01_start_prod.sh
```

### Locust load test
```py
conda activate bench
sh scripts/02_locust.sh
```
