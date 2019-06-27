class NetworkDevice:
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        
        self.serial_number = ""
        self.model = ""
        self.vendor = ""
        self.uptime = ""
        self.os_version = ""
    def ip(self):
        print(f"The ip address for this device is {self.ip_addr}")
    def username_pass(self):
        print(f"The username is {self.username}, and the password is {self.password}")
    def assign_vendor(self, vendor):
        self.vendor = vendor
        print(f"Set the vendor is {vendor}")

nd1 = NetworkDevice('10.1.1.1', 'admin1', 'password1')
nd2 = NetworkDevice('10.2.2.2', 'admin2', 'password2')
nd3 = NetworkDevice('10.3.3.3', 'admin3', 'password3')
nd4 = NetworkDevice('10.4.4.4', 'admin4', 'password4')

nd1.ip()
nd1.username_pass()
nd1.assign_vendor("Cisco")
