import logging

from iterative_metrics.main import main


class TestMain:
    """End-to-end integration test for the main function."""

    def test_main(self, caplog):
        caplog.set_level(logging.INFO, logger="iterative_metrics")

        main()

        assert "43 work items found" in caplog.text
        assert "17 potential workflow steps found" in caplog.text
        assert (
            "board status: [12, 16, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 3, 0, 2, 0]"
            in caplog.text
        )
