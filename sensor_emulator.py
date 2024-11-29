import random
import time
from datetime import datetime


def emulate_sensor(min_value, max_value, metric_name, unit, output_file):
    data_points = []
    while True:
        value = random.uniform(min_value, max_value)
        data_points.append(value)

        if len(data_points) == 60:
            avg_value = sum(data_points) / len(data_points)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            record = (
                f"{current_time}\t|\t{metric_name}\t|\t{avg_value:.2f}\t|\t"
                f"{unit}\t|\n"
            )

            with open(output_file, 'a') as f:
                f.write(record)

            data_points = []

        time.sleep(1)


if __name__ == "__main__":
    min_value = float(input("Введите минимальное значение: "))
    max_value = float(input("Введите максимальное значение: "))
    metric_name = input("Введите название метрики: ")
    unit = input("Введите единицу измерения: ")
    output_file = "sensor_data.csv"

    emulate_sensor(min_value, max_value, metric_name, unit, output_file)
