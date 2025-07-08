# Default values
script_name=$0
DOCKER_IMAGE_NAME='nvcr.io/nvidian/isaac-sdk/isaac_arena'
TAG='development'

SCRIPT_DIR="$(dirname "${BASH_SOURCE}")"

push=false

# Default mount directory on the host machine for the datasets
DATASETS_HOST_MOUNT_DIRECTORY="$HOME/datasets"
# Default mount directory on the host machine for the models
MODELS_HOST_MOUNT_DIRECTORY="$HOME/models"
# Default mount directory on the host machine for the evaluation directory
EVAL_HOST_MOUNT_DIRECTORY="$HOME/eval"

while getopts ":hptn:" OPTION; do
    case $OPTION in

        d)
            DATASETS_HOST_MOUNT_DIRECTORY=$OPTARG
            ;;
        m)
            MODELS_HOST_MOUNT_DIRECTORY=$OPTARG
            ;;
        e)
            EVAL_HOST_MOUNT_DIRECTORY=$OPTARG
            ;;
        p)
            push=true
            ;;
        t)
            TAG=${OPTARG}
            ;;
        n)
            DOCKER_IMAGE_NAME=${OPTARG}
            ;;
        h | *)
            echo "Helper script to build $DOCKER_IMAGE_NAME (default)"
            echo "Usage:"
            echo "$script_name -h"
            echo "$script_name -p"
            echo "$script_name -t <tag>"
            echo "$script_name -n <docker name>"
            echo ""
            echo "  -p Push image to $DOCKER_IMAGE_NAME after building"
            echo "  -h help (this output)"
            echo "  -t <tag> (default is $TAG)"
            echo "  -n <docker name> (default is $DOCKER_IMAGE_NAME)"
            exit 0
            ;;
    esac
done

# Display the values being used
echo "Using Docker name: $DOCKER_IMAGE_NAME"
echo "Using tag: $TAG"

# Login to Docker registry
docker login nvcr.io

# Build the Docker image with the specified or default name and tag
docker build --pull -t ${DOCKER_IMAGE_NAME}:${TAG} --file $SCRIPT_DIR/Dockerfile.isaac_arena $SCRIPT_DIR/..

if $push ; then
    echo "Pushing to $DOCKER_IMAGE_NAME:${TAG}"
    docker push $DOCKER_IMAGE_NAME:${TAG}
fi

DOCKER_RUN_ARGS=("--privileged"
                "--ulimit" "memlock=-1"
                "--ulimit" "stack=-1"
                "--ipc=host"
                "--net=host"
                "--runtime=nvidia"
                "--gpus=all"
                "-v" ".:/workspaces/isaac_arena"
                "-v" "$DATASETS_HOST_MOUNT_DIRECTORY:/datasets"
                "-v" "$MODELS_HOST_MOUNT_DIRECTORY:/models"
                "-v" "$EVAL_HOST_MOUNT_DIRECTORY:/eval"
                "-v" "$HOME/.bash_history:/home/$(id -un)/.bash_history"
                "-v" "$HOME/.config/osmo:/home/$(id -un)/.config/osmo"
                "-v" "/tmp:/tmp"
                "-v" "/tmp/.X11-unix:/tmp/.X11-unix:rw"
                "-v" "/var/run/docker.sock:/var/run/docker.sock"
                "-v" "$HOME/.Xauthority:/root/.Xauthority"
                "--env" "DISPLAY"
                "--env" "ACCEPT_EULA=Y"
                "--env" "PRIVACY_CONSENT=Y"
                "--env" "DOCKER_RUN_USER_ID=$(id -u)"
                "--env" "DOCKER_RUN_USER_NAME=$(id -un)"
                "--env" "DOCKER_RUN_GROUP_ID=$(id -g)"
                "--env" "DOCKER_RUN_GROUP_NAME=$(id -gn)"
                "--env" "OMNI_USER=\$omni-api-token"
                "--env" "OMNI_PASS=$OMNI_PASS"
                "--env" "OMNI_KIT_ALLOW_ROOT=1"
                )

# Allow X11 connections
xhost +local:docker

docker run "${DOCKER_RUN_ARGS[@]}" --interactive --rm --tty ${DOCKER_IMAGE_NAME}:${TAG}
