from os import system

def Main():
    print("wifipumpkin3 easy script by cvip\n")
    ssid = input("What do you want the ssid name to be 'The name of the wifi' > ")
    system("iwconfig")
    interface = input("\nWhat wifi interface will host the RAP > ")
    print("""\n
    Proxies
    =======
    captiveflask (Allow block Internet access for users until they open the page login page.)
    phishkin3 (Proxy for create captive portal with external phishing page)
    evilqr3 (Proxy for create captive portal QR phishing WhatsApp,Discord, etc... )
    pumpkinproxy (Transparent proxies that you can use to intercept and manipulate HTTP traffic modifying requests and responses, that allow to inject javascripts into the targets visited.)
    noproxy (Runnning without proxy redirect traffic)\n
    """)
    proxies = input("What proxy do you want to use > ")

    proxy_commands = {
        'captiveflask': {
            'message': 'Captive Portal plugins (You might need to install some of them) used as fake login pages',
            'prefix': 'captiveflask.',
            'options': [
                'DarkLogin',
                'FlaskDemo',
                'Login_v4',
                'example',
                'facebook',
                'loginPage',
                'microsoft'
            ]
        },
        'pumpkinproxy': {
            'message': 'PumpkinProxy 3 plugins',
            'prefix': 'pumpkinproxy.',
            'options': [
                'beef',
                'downloadspoof',
                'html_inject',
                'js_inject',
                'no-cache'
            ]
        }
    }

    if proxies in proxy_commands:
        proxy_data = proxy_commands[proxies]
        print(f"\n{proxy_data['message']}")
        print("Options:")
        for option in proxy_data['options']:
            print(f" - {option}")
        plugin = input(f"What {proxies} plugin do you want to use > ")
        print("\nLaunching program\n")
        system(f'sudo wifipumpkin3 --xpulp "set interface {interface}; set ssid {ssid}; set proxy {proxies}; set {proxy_data["prefix"]}{plugin}; start"')
    else:
        print("\nLaunching program\n")
        system(f'sudo wifipumpkin3 --xpulp "set interface {interface}; set ssid {ssid}; set proxy {proxies}; start"')

if __name__ == "__main__":
    Main()
