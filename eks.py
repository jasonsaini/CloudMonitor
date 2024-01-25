from kubernetes import client, config
APP_NAME = "my-flask-app"
IMAGE_URI = "851725446852.dkr.ecr.us-east-1.amazonaws.com/my-cloud-native-repo:latest"
CONTAINER_PORT = 5000
config.load_kube_config()

api_client = client.ApiClient()

deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name=APP_NAME),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": APP_NAME}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": APP_NAME}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name=APP_NAME,
                        image=IMAGE_URI,
                        ports=[client.V1ContainerPort(container_port=CONTAINER_PORT)]
                    )
                ]
            )
        )
    )
)

api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace='default', 
    body=deployment
)

service = client.V1Service(
    metadata=client.V1ObjectMeta(name=APP_NAME),
    spec=client.V1ServiceSpec(
        selector={"app":APP_NAME},
        ports=[client.V1ServicePort(port=CONTAINER_PORT)]
    )
)

api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default", 
    body=service
)