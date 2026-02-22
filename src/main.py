from datetime import datetime, timezone


def main() -> None:
    print("wearable-anomaly-detection-platform initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
