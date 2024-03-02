from flask import Flask
import requests

app = Flask(__name__)


def control_containers(action, distro):
    endpoint = "http://127.0.0.1:2375"

    if action == "start":
        response = requests.post(
            f"{endpoint}/containers/create?name={distro.lower()}",
            json={
                "Image": distro.lower()
            }
        )

        container_id = response.json()["Id"]
        requests.post(f"{endpoint}/containers/{container_id}/start")
        return f"Container {distro.lower()} started."

    if action == "stop":
        requests.post(f"{endpoint}/containers/{distro.lower()}/stop")
        return f"Container {distro.lower()} stopped."

    raise Exception("Invalid action.")


@app.route("/control/<action>/<distro>")
def control(action, distro):
    return control_containers(action, distro)


if __name__ == "__main__":
    app.run(debug=True)
