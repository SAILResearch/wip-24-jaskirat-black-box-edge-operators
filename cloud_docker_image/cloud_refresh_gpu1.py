from flask import Flask, request
import docker
from subprocess import Popen, PIPE

app = Flask(__name__)
client = docker.from_env()

@app.route('/stop_container', methods=['POST'])
def stop_container():
    container_name = request.form.get('container_name')
    try:
        container = client.containers.get(container_name)
        container.stop()
        return f"Container '{container_name}' stopped successfully."
    except docker.errors.NotFound:
        return f"Container '{container_name}' not found."
    except docker.errors.APIError as e:
        return f"Error stopping container: {str(e)}"


@app.route('/restart_container', methods=['POST'])
def restart_container():
    container_name = request.form.get('container_name')
    try:
        container = client.containers.get(container_name)
        container.restart()
        docker_command = f'docker exec -d {container_name} bash -c "chmod +x ./network.sh;./network.sh"'
        process = Popen(docker_command, shell=True, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if error:
            return f"Error running the network script: {error.decode('utf-8')}"
        else:
            return f"Container '{container_name}' restarted successfully and Network script successfully executed!"
    except docker.errors.NotFound:
        return f"Container '{container_name}' not found."
    except docker.errors.APIError as e:
        return f"Error restarting container: {str(e)}"

@app.route('/restart_container_10mbps', methods=['POST'])
def restart_container_10mbps():
    container_name = request.form.get('container_name')
    try:
        container = client.containers.get(container_name)
        container.restart()
        docker_command = f'docker exec -d {container_name} bash -c "chmod +x ./network_10mbps.sh;./network_10mbps.sh"'
        process = Popen(docker_command, shell=True, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if error:
            return f"Error running the network script: {error.decode('utf-8')}"
        else:
            return f"Container '{container_name}' restarted successfully and Network script successfully executed!"
    except docker.errors.NotFound:
        return f"Container '{container_name}' not found."
    except docker.errors.APIError as e:
        return f"Error restarting container: {str(e)}"

@app.route('/restart_container_50mbps', methods=['POST'])
def restart_container_50mbps():
    container_name = request.form.get('container_name')
    try:
        container = client.containers.get(container_name)
        container.restart()
        docker_command = f'docker exec -d {container_name} bash -c "chmod +x ./network_50mbps.sh;./network_50mbps.sh"'
        process = Popen(docker_command, shell=True, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if error:
            return f"Error running the network script: {error.decode('utf-8')}"
        else:
            return f"Container '{container_name}' restarted successfully and Network script successfully executed!"
    except docker.errors.NotFound:
        return f"Container '{container_name}' not found."
    except docker.errors.APIError as e:
        return f"Error restarting container: {str(e)}"

@app.route('/restart_container_100mbps', methods=['POST'])
def restart_container_100mbps():
    container_name = request.form.get('container_name')
    try:
        container = client.containers.get(container_name)
        container.restart()
        docker_command = f'docker exec -d {container_name} bash -c "chmod +x ./network_100mbps.sh;./network_100mbps.sh"'
        process = Popen(docker_command, shell=True, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if error:
            return f"Error running the network script: {error.decode('utf-8')}"
        else:
            return f"Container '{container_name}' restarted successfully and Network script successfully executed!"
    except docker.errors.NotFound:
        return f"Container '{container_name}' not found."
    except docker.errors.APIError as e:
        return f"Error restarting container: {str(e)}"

@app.route('/restart_container_150mbps', methods=['POST'])
def restart_container_150mbps():
    container_name = request.form.get('container_name')
    try:
        container = client.containers.get(container_name)
        container.restart()
        docker_command = f'docker exec -d {container_name} bash -c "chmod +x ./network_150mbps.sh;./network_150mbps.sh"'
        process = Popen(docker_command, shell=True, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if error:
            return f"Error running the network script: {error.decode('utf-8')}"
        else:
            return f"Container '{container_name}' restarted successfully and Network script successfully executed!"
    except docker.errors.NotFound:
        return f"Container '{container_name}' not found."
    except docker.errors.APIError as e:
        return f"Error restarting container: {str(e)}"

@app.route('/restart_container_200mbps', methods=['POST'])
def restart_container_200mbps():
    container_name = request.form.get('container_name')
    try:
        container = client.containers.get(container_name)
        container.restart()
        docker_command = f'docker exec -d {container_name} bash -c "chmod +x ./network_200mbps.sh;./network_200mbps.sh"'
        process = Popen(docker_command, shell=True, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if error:
            return f"Error running the network script: {error.decode('utf-8')}"
        else:
            return f"Container '{container_name}' restarted successfully and Network script successfully executed!"
    except docker.errors.NotFound:
        return f"Container '{container_name}' not found."
    except docker.errors.APIError as e:
        return f"Error restarting container: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True)
