from prefect import flow

from prefect_testing.tasks import (
    goodbye_prefect_testing,
    hello_prefect_testing,
)


def test_hello_prefect_testing():
    @flow
    def test_flow():
        return hello_prefect_testing()

    result = test_flow()
    assert result == "Hello, prefect-testing!"


def goodbye_hello_prefect_testing():
    @flow
    def test_flow():
        return goodbye_prefect_testing()

    result = test_flow()
    assert result == "Goodbye, prefect-testing!"
