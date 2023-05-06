from time import timezone

from cronman.job import BaseCronJob, cron_job_registry

class HelloWorld(BaseCronJob):
    """Demo Cron Job class"""

    def run(self):
        """Main logic"""
        pass

cron_job_registry.register(HelloWorld, name='Hello')

def test_cron_run():
    print("\n\nHello World....!! ",timezone.now())

CRON_JOBS = (
    ...
    # (<time spec>, <job spec>)
    # 'HelloWorld' will be executed a 5:15AM every day:
    ('   *   *   *   *   *', 'HelloWorld'),
)