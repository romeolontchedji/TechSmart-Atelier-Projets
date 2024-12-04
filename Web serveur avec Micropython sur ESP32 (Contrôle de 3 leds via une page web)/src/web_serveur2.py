import network
import socket
from machine import Pin

# Configuration des broches pour les LEDs
led1 = Pin(15, Pin.OUT)
led2 = Pin(4, Pin.OUT)
led3 = Pin(5, Pin.OUT)

# Configuration du point d'accès
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="ESP32-AP", password="12345678")

while not ap.active():
    pass
print("Point d'accès actif")
print(ap.ifconfig())

# Page HTML
def web_page():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ESP32 LED Control</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            h1 {
                color: #333;
                margin-top: 20px;
            }
            .led-control {
                display: flex;
                justify-content: center;
                margin: 20px;
                flex-wrap: wrap;
            }
            .led {
                margin: 10px;
                padding: 10px;
                background-color: #fff;
                border: 2px solid #ccc;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            .led p {
                font-size: 18px;
                color: #444;
            }
            button {
                padding: 10px 20px;
                margin: 5px;
                font-size: 16px;
                cursor: pointer;
                border: none;
                border-radius: 5px;
            }
            .btn-on {
                background-color: #4CAF50;
                color: white;
            }
            .btn-on:hover {
                background-color: #45a049;
            }
            .btn-off {
                background-color: #f44336;
                color: white;
            }
            .btn-off:hover {
                background-color: #d32f2f;
            }
        </style>
    </head>
    <body>
        <h1>ESP32 LED Control</h1>
        <div class="led-control">
            <div class="led">
                <p>LED 1</p>
                <button class="btn-on" onclick="sendRequest('/?led1=on')">ON</button>
                <button class="btn-off" onclick="sendRequest('/?led1=off')">OFF</button>
            </div>
            <div class="led">
                <p>LED 2</p>
                <button class="btn-on" onclick="sendRequest('/?led2=on')">ON</button>
                <button class="btn-off" onclick="sendRequest('/?led2=off')">OFF</button>
            </div>
            <div class="led">
                <p>LED 3</p>
                <button class="btn-on" onclick="sendRequest('/?led3=on')">ON</button>
                <button class="btn-off" onclick="sendRequest('/?led3=off')">OFF</button>
            </div>
        </div>
        <script>
            function sendRequest(url) {
                fetch(url).then(response => response.text()).then(data => {
                    console.log(data);
                });
            }
        </script>
    </body>
    </html>
    """
    return html

# Serveur web
def serve():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Serveur en écoute sur', addr)

    while True:
        cl, addr = s.accept()
        print('Client connecté de', addr)
        request = cl.recv(1024).decode('utf-8')
        print('Requête:', request)

        # Lecture des paramètres de la requête
        if '/?led1=on' in request:
            led1.value(1)
        elif '/?led1=off' in request:
            led1.value(0)
        elif '/?led2=on' in request:
            led2.value(1)
        elif '/?led2=off' in request:
            led2.value(0)
        elif '/?led3=on' in request:
            led3.value(1)
        elif '/?led3=off' in request:
            led3.value(0)

        # Réponse HTML
        response = web_page()
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n' + response)
        cl.close()

try:
    serve()
except KeyboardInterrupt:
    print("Serveur arrêté")
