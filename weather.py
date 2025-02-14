import adafruit_bme680
import time
import board

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25
i = 0
while i < 3: 
		print("\n", time.ctime(),"Temperature %0.1f C" % bme680.temperature,"Gas %d ohm" % bme680.temperature,"Humidity: %0.1f %%" % bme680.relative_humidity,"Pressure: %0.3f hPa" % bme680.pressure,"Altitude = %0.2f meters" % bme680.altitude,time.ctime())
		i = i + 1
		time.sleep(2)
	

	

