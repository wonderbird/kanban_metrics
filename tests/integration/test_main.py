import logging

from iterative_metrics.main import main


class TestMain:
    """End-to-end integration test for the main function."""

    def test_main(self, caplog):
        caplog.set_level(logging.INFO, logger="iterative_metrics")

        main()

        assert "board status: [11, 6, 10, 4, 9, 4, 11, 9, 1]" in caplog.text
