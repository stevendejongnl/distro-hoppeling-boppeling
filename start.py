import os
import subprocess


PWD = os.path.realpath(__file__)


def build_container(distro: str):
    dockerfile_path = os.path.join(
        os.path.dirname(PWD), "distros/ubuntu/Dockerfile"
    )
    print(f"{dockerfile_path=}")
    subprocess.run([
        "docker", "build",
        "-t", distro.lower(),
        dockerfile_path,
    ])


def run_container(distro: str):
    pass


if __name__ == "__main__":
    distro = "ubuntu"
    build_container(distro=distro)
    run_container(distro=distro)
