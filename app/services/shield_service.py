import time

import smbus2


class ShieldService:
    __CMD_SERVO1 = 0
    __CMD_SERVO2 = 1
    __CMD_SERVO3 = 2
    __CMD_SERVO4 = 3
    __CMD_PWM1 = 4
    __CMD_PWM2 = 5
    __CMD_DIR1 = 6
    __CMD_DIR2 = 7
    __CMD_BUZZER = 8
    __CMD_IO1 = 9
    __CMD_IO2 = 10
    __CMD_IO3 = 11
    __CMD_SONIC = 12

    __SONIC_MAX_HIGH_BYTE = 50

    def __init__(self, addr=0x18):
        self.address = addr  # default address of mDEV
        self.bus = smbus2.SMBus(1)
        self.bus.open(1)

    def get_sonic_echo_time(self):
        return self.__read_reg(self.__CMD_SONIC)

    def get_sonic(self):
        sonic_echo_time = self.__read_reg(self.__CMD_SONIC)
        return sonic_echo_time * 17.0 / 1000.0

    def set_motor_speed(self, speed, direction):
        self.__write_reg(self.__CMD_DIR1, direction)
        self.__write_reg(self.__CMD_DIR2, direction)

        self.__write_reg(self.__CMD_PWM1, speed)
        self.__write_reg(self.__CMD_PWM2, speed)

    def set_steering_direction(self, value):
        cnt = 3
        while cnt != 0:
            cnt = cnt - 1
            for i in range(50, 140, 1):
                self.__write_reg(self.__CMD_SERVO1, int(self.num_map(i, 0, 180, 500, 2500)))
                time.sleep(0.005)
            for i in range(140, 50, -1):
                self.__write_reg(self.__CMD_SERVO1, int(self.num_map(i, 0, 180, 500, 2500)))
                time.sleep(0.005)
        self.__write_reg(self.__CMD_SERVO1, int(self.num_map(90, 0, 180, 500, 2500)))

    def num_map(self, value, from_low, from_high, to_low, to_high):
        return (to_high - to_low) * (value - from_low) / (from_high - from_low) + to_low

    def __set_shield_i2c_address(self, addr):  # addr: 7bit I2C Device Address
        if (addr < 0x03) or (addr > 0x77):
            return
        else:
            self.__write_reg(0xaa, (0xbb << 8) | (addr << 1))

    def __write_reg(self, cmd, value):
        try:
            self.bus.write_i2c_block_data(self.address, cmd, [value >> 8, value & 0xff])
            time.sleep(0.001)
            self.bus.write_i2c_block_data(self.address, cmd, [value >> 8, value & 0xff])
            time.sleep(0.001)
            self.bus.write_i2c_block_data(self.address, cmd, [value >> 8, value & 0xff])
            time.sleep(0.001)
        except Exception, e:
            print Exception, "I2C Error :", e

    def __read_reg(self, cmd):
        for i in range(0, 10, 1):
            self.bus.write_i2c_block_data(self.address, cmd, [0])
            a = self.bus.read_i2c_block_data(self.address, cmd, 1)

            self.bus.write_byte(self.address, cmd + 1)

            self.bus.write_byte(self.address, cmd)
            c = self.bus.read_byte_data(self.address, cmd)

            self.bus.write_byte(self.address, cmd + 1)
            d = self.bus.read_byte_data(self.address, cmd + 1)

            if a[0] == c and c < self.__SONIC_MAX_HIGH_BYTE:
                return c << 8 | d
            else:
                continue

        return 0
