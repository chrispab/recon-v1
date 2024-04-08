# https://doc.qt.io/qtforpython-6/tutorials/datavisualize/filter_data.html

import argparse
import pandas as pd

from PySide6.QtCore import QDateTime, QTimeZone


def transform_date(utc, timezone=None):
    # utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
    # new_date = QDateTime().fromString(utc, utc_fmt)

    # 2018-12-11T21:14:44.682Z
    # 2024-02-21 11:31:10
    fmt = "yyyy-MM-dd HH:mm:ss"
    new_date = QDateTime().fromString(utc, fmt)

    if timezone:
        new_date.setTimeZone(timezone)
    return new_date


def read_data(fname):
    # Read the CSV content
    df = pd.read_csv(fname)

    # Remove wrong magnitudes
    df = df.drop(df[df.mainamount < 50].index)
    mainamounts = df["mainamount"]

    # My local timezone
    timezone = QTimeZone(b"Europe/Berlin")

    # Get timestamp transformed to our timezone
    times = df["transactionstartedtimestamp"].apply(
        lambda x: transform_date(x, timezone)
    )

    return times, mainamounts


if __name__ == "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)
    print(data)
