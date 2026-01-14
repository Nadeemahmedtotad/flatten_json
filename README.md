# Flattened JSON Service — Production-Style Backend System

This project is a production-style backend system built using **FastAPI**, **Celery**, **Redis**, **Docker**, **OpenTelemetry**, **VictoriaMetrics**, **Grafana**, and **Locust**.

It demonstrates authenticated APIs, background job processing, observability, monitoring, and load testing using modern backend engineering practices.

---

## Features

- Authenticated API to flatten nested JSON
- Mock login API
- Asynchronous background jobs using Celery
- IP anomaly detection via Celery tasks
- Metrics collection using OpenTelemetry
- Metrics storage using VictoriaMetrics
- Visualization using Grafana
- Load testing using Locust
- Fully Dockerized setup

---

## System Architecture

Locust → FastAPI → Celery → Redis → OpenTelemetry → VictoriaMetrics → Grafana

---

## APIs

### Login API
POST /login

- Accepts username and password
- Assumes credentials are always valid
- Triggers a background Celery task

### Flatten JSON API (Protected)
POST /flatten

Flattens nested JSON into a single-level JSON.

---

## Monitoring & Observability

- Metrics exposed at /metrics
- Stored in VictoriaMetrics
- Visualized in Grafana
- Celery monitored using Flower

---

## Load Testing

- Dockerized Locust
- Simulates concurrent users
- Observed via Grafana dashboards

---

## How to Run

docker compose up --build

---

## Service Ports

FastAPI: http://localhost:8000  
Grafana: http://localhost:3000  
VictoriaMetrics: http://localhost:8428  
Flower: http://localhost:5555  
Locust: http://localhost:8089  

---

## Author

Nadeemahmed Totad
