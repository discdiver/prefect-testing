"""This is an example flows module"""
from prefect import flow

from prefect_testing.blocks import TestingBlock
from prefect_testing.tasks import (
    goodbye_prefect_testing,
    hello_prefect_testing,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    TestingBlock.seed_value_for_example()
    block = TestingBlock.load("sample-block")

    print(hello_prefect_testing())
    print(f"The block's value: {block.value}")
    print(goodbye_prefect_testing())
    return "Done"


if __name__ == "__main__":
    hello_and_goodbye()
