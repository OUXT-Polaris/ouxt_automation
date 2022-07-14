minikube start
kubectl create ns argo
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/stable/manifests/quick-start-postgres.yaml
kubectl create ns minio-trained-weights
kubectl apply -f manifests/minio-trained-weights.yaml