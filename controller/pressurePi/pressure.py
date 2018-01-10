import spidev, time
spi = spidev.SpiDev()

spi.open(0,0)

def analog_read(channel):
	r = spi.xfer2([4 | 2 |(channel>>2), (channel &3) << 6,0])
	adc_out = ((r[1]&15) << 8) + r[2]
	return adc_out

while True:
	sensorVal=analog_read(0)	#PressureSensor
	voltage = (sensorVal*5.0)/1024.0
	pressure_pascal = (3.0*((float)voltage-0.47))*1000000.0
	pressure_bar = pressure_pascal/10e5
	print("Reading=%d\tVoltage=%f\tPascal=%f\tBar=%f" % (sensorVal,voltage,pressure_pascal,pressure_bar)) 
	time.sleep(1)