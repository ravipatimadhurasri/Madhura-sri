from flask import Flask

app = Flask(_name_)


@app.get("/")
def hello_world() -> tuple[str, int, dict[str, str]]:
    return "Hello World RAVIPATI", 250, {"Content-Type": "text/plain; charset=utf-8"}


if _name_ == "_main_":
    # Bind to all interfaces so it works in Docker/Kubernetes.
    app.run(host="0.0.0.0", port=5000)
