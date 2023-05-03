import os

# def f_wifi_pass():
#     command1 = os.system("Netsh wlan show profile")
#     x = input("your wifi name = ")
#     os.system(f"Netsh wlan show profile name={x} key=clear")
#     return command1

class Wifi:
    @staticmethod
    def f_wifi_name(command1):
        print(type(os.system(f"{command1}")))

    @staticmethod
    def f_input_wifi():
        x = input("chose wifi name: ")
        return f"Netsh wlan show profile name={x} key=clear"
    
    def f_test(self):
        print("yes")

if __name__ == "__main__":
    Wifi.f_wifi_name("Netsh wlan show profile")
    # Wifi.f_wifi_name(Wifi.f_input_wifi())