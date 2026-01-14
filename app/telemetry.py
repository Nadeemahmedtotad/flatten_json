from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor


def setup_telemetry(app):
    resource = Resource.create({
        "service.name": "flattened-json-service"
    })

    reader = PrometheusMetricReader()

    provider = MeterProvider(
        resource=resource,
        metric_readers=[reader],
    )

    metrics.set_meter_provider(provider)

    # Auto-instrument FastAPI
    FastAPIInstrumentor.instrument_app(app)
