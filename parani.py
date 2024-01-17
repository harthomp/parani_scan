import serial


import payloads

# DESIGN IDEA, MAKE IT SO THAT YOU PASS BOOL TO METHOD OR CLASS (FOR CLASS WOULD HAVE TO BE FOR COMMANDS ONLY AND NO RESPONSE TO VALIDATE COMMANDS - THINK UDP) TO GET THE RESPONSE OR NOT - RIGHT NOW BIGGEST TIME BOTTLENECK

class Parani_SD1000:
    def __init__(self):
        self.serial_line = serial.Serial(
                port = "/dev/ttyUSB0",
                baudrate = 57600,
                write_timeout = None,
                timeout = 5
                )
        
        self.response = None


    # 1000 used for read param now as unsure of sizing reqs. 

    def bt_info(self):
        self.serial_line.write(payloads.BT_INFO)
        self.response = self.serial_line.read(1000)

    def bt_inq(self):
        self.serial_line.write(payloads.BT_INQ)
        self.response = self.serial_line.read(1000)
    
    def atz(self):
        self.serial_line.write(payloads.ATZ)
        self.response = self.serial_line.read(1000)
   
    # Does mode even matter for the scanning???? Perhaps only the pending status blocks. 3 was the default on dongle. - It does not matter at all for scanning. Pending status is what prevents commands
    # Need to check if mode in range 0-3
    def bt_mode(self, mode: int):
        self.serial_line.write(payloads.BT_MODE[mode])
        self.response = self.serial_line.read(1000)

    def bt_cancel(self):
        self.serial_line.write(payloads.BT_CANCEL)
        self.response = self.serial_line.read(1000)
