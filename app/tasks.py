from app.celery_app import celery_app
from app.constants import KNOWN_IPS


@celery_app.task
def check_ip(username: str, current_ip: str):
    # print(
    #         f"⚠️ UNKNOWN IP LOGIN DETECTED "
    #         f"user={username}, ip={current_ip}"
    #     )
    if current_ip not in KNOWN_IPS:
        print(
            f"⚠️ UNKNOWN IP LOGIN DETECTED "
            f"user={username}, ip={current_ip}"
        )
