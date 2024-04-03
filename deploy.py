import sys
from hello_world import my_flow

image = sys.argv[1]

my_flow.deploy(
    name="my-docker-deployment",
    work_pool_name="Test",
    tags=["onboarding"],
    parameters={"value": 1},
    interval=60,
    image=image,
)
