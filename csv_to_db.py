import csv
import glob
import datetime
import os
import sqlite3


# def generate_price_from_csv_file(csv_file_name="1301_1983.csv", code="1301"):
def generate_price_from_csv_file(csv_file_name="1301_1983.csv", code="1301"):
    with open(csv_file_name, encoding="shift_jis") as f:
        reader = csv.reader(f)
        next(reader) # 先頭行は飛ばす
        next(reader) # 2行目も飛ばす
        for row in reader:
            # day = datetime.datetime.strptime(row[0], '%Y/%m/%d').date()  # 日付
            day = row[0]
            open_ = float(row[1])  # 始値
            high = float(row[2])  # 高値
            low = float(row[3])  # 高値
            close = float(row[4])  # 終値
            volume = int(row[5])  # 出来高
            adjustment = float(row[6])  # 終値調整値
            # 日付, 始値, 高値, 安値, 終値, 出来高, 終値調整値
            # print("day: " + str(day) + ";open: " + str(open_) + ";high: " + str(high) + ";low: " + str(low) + ";close: " + str(close) + ";volume: " + str(volume) + ";adjustment: " + str(adjustment))
            yield code, day, open_, high, low, close, volume, adjustment


def generate_from_csv_dir(csv_dir, generate_func):
    for path in glob.glob(os.path.join(csv_dir, "*.T.csv")):
        file_name = os.path.basename(path)
        code = file_name.split('.')[0]
        for d in generate_func(path, code):
            yield d


if __name__ == '__main__':
    gen = generate_price_from_csv_file("1301_1983.csv", 1301)
    for e in gen:
        print(e)
