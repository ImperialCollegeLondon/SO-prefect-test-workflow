from prefect import flow, task


@task
def hello(value: int) -> int:
    return value


@task
def goodbye(value: int) -> int:
    return value * 2


@flow(log_prints=True)
def my_flow(value: int):
    goodbye(hello(value))
