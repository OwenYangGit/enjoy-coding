from flask import Flask

app = Flask("__name__")

# 測試用 API
@app.route("/")
def main():
    return "Hello World"

if __name__ == "__main__":
    app.run()