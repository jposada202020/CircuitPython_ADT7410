# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import adt7410

i2c = board.I2C()  # uses board.SCL and board.SDA
adt = adt7410.ADT7410(i2c)

while True:
    temp = adt.temperature
    print("Temperature :{:.2f}C".format(temp))
    time.sleep(0.5)
