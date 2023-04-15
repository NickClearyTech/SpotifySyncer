from celery_settings import app as celery_app


@celery_app.task(bind=True)
def test(self):
    print("hi")
