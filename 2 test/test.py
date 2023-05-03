import wifi_pass

x = wifi_pass.Wifi()

x.f_wifi_name("Netsh wlan show profile")
x.f_wifi_name(x.f_input_wifi())
