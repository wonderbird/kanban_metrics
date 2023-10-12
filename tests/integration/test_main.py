import logging

from iterative_metrics.main import main


class TestMain:
    """End-to-end integration test for the main function."""

    def test_main(self, caplog):
        caplog.set_level(logging.INFO, logger="iterative_metrics")

        main()

        assert (
            "board status: [12, 16, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 3, 0, 2, 0]"
            in caplog.text
        )
