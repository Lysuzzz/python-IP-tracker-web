from flask import Flask, request

app = Flask(__name__)

def get_real_ip():
    # Zuerst prüfen, ob der Benutzer hinter einem Proxy oder Load Balancer ist
    if request.headers.get('X-Forwarded-For'):
        # Wenn 'X-Forwarded-For' existiert, steht die reale IP normalerweise hier drin
        ip = request.headers.getlist('X-Forwarded-For')[0]
    else:
        # Ansonsten einfach die Remote-Adresse verwenden
        ip = request.remote_addr
    return ip

@app.route('/')
def log_ip():
    # IP-Adresse des Besuchers erfassen
    user_ip = get_real_ip()

    # IP-Adresse speichern
    with open("ips.txt", "a") as f:
        f.write(f"IP: {user_ip}\n")
    
    return f"Deine IP {user_ip} wurde protokolliert!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # '0.0.0.0' ermöglicht externen Zugriff
