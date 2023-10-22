import logging

from iterative_metrics.main import main


class TestMain:
    """End-to-end integration test for the main function."""

    def test_main(self, caplog):
        caplog.set_level(logging.INFO, logger="iterative_metrics")

        main()

        # As long as the documentation areas are considered as workflow steps,
        # the following board status should be reported.
        assert "board status: [0, 11, 6, 0, 10, 5, 0, 9, 4, 11, 9, 1]" in caplog.text

        # When documentation areas are ignored in workflow steps,
        # the following board status should be reported.
        # assert "board status: [11, 6, 10, 4, 9, 4, 11, 9, 1]" in caplog.text
