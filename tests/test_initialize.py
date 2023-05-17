from pytest import raises

from address_scraper.address_scraper.initialize import (MAX_API_REQUESTS,
                                                        MAX_PAYLOAD_LIMIT,
                                                        setup_args)


def test_setup_args():
    args = ["-s", "NY", "-t", "100", "-l", "100"]
    args_obj = setup_args(args)

    assert args_obj.state == "NY"
    assert args_obj.limit == 100
    assert args_obj.total == 100
    assert args_obj.verbose is False
    assert args_obj.map is False

    args_obj = setup_args(["-s", "NY", "-t", "100", "-l", "100", "-v", "-m"])
    assert args_obj.verbose is True
    assert args_obj.map is True

    args_obj = setup_args(["-s", "NY"])
    assert args_obj.limit == MAX_PAYLOAD_LIMIT
    assert args_obj.total == MAX_API_REQUESTS
    assert args_obj.verbose is False
    assert args_obj.map is False


def test_system_exit():
    with raises(SystemExit):
        setup_args([])

    with raises(SystemExit):
        setup_args(["-s", "NY", "-t", "-100", "-l", "100"])


def test_ignore_state_code():
    args_obj = setup_args(["-s", "12"])
    assert args_obj.state == "12"
    assert args_obj.limit == MAX_PAYLOAD_LIMIT
    assert args_obj.total == MAX_API_REQUESTS
    assert args_obj.verbose is False
    assert args_obj.map is False
