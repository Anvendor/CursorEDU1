from abc import ABC, abstractmethod


class LaptopInterface(ABC):

    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

    @abstractmethod
    def touchpad(self):
        pass

    @abstractmethod
    def webcam(self):
        pass

    @abstractmethod
    def ports(self):
        pass

    @abstractmethod
    def dynamics(self):
        pass


class HLaptop(LaptopInterface):

    def __init__(self, model):
        self.model = model

    def screen(self):
        print(f"{self.model} has a 16-inch FHD IPS display.")

    def keyboard(self):
        print(f"{self.model} has a full-size backlit keyboard.")

    def touchpad(self):
        print(f"{self.model} has glass touchpad with Multi-touch, Huawei Share Built-in.")

    def webcam(self):
        print(f"{self.model} has a 720P HP Recessed camera .")

    def ports(self):
        print(f"{self.model} has USB-C x 2 (support data, charging and DisplayPort);USB3.2 Gen1 x 2;HDMI x 1;3.5 mm headset and microphone 2-in-1 jack x 1.")

    def dynamics(self):
        print(f"{self.model} has Speaker x 2.")

h_laptop = HLaptop("HUAWEI NateBook 16")

h_laptop.screen()
h_laptop.keyboard()
h_laptop.touchpad()
h_laptop.webcam()
h_laptop.ports()
h_laptop.dynamics()
