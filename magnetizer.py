import time
import board
import busio
import adafruit_tlv493d
i2c = busio.I2C(board.SCL, board.SDA)
tlv = adafruit_tlv493d.TLV493D(i2c)

print("X: %s, Y: %s, Z: %s mT"%tlv.magnetic)

