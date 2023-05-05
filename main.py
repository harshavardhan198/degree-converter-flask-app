from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    celsius = (request.args.get("celsius", ""))
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else :
        fahrenheit = ""
    return (
        """<form action="" method="get">
            Celsius temperature: <input type="text" name = "celsius">
            </form>"""
        + "Fahrenheit: "
        + fahrenheit
    )
@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    try:
        fahrenheit = float(celsius) * 9/5 + 32
        fahrenheit = round(fahrenheit,3)
        return str(fahrenheit)
    except ValueError:
        return "invalid input"
    
if __name__ == "__main__":
    # celsius = input("Celsius: ")
    # print("Fahrenheit: ", fahrenheit_from(celsius))
    app.run(host = "127.0.0.1", port = 8000, debug = True)
