## NS 
kubectl create namespace monitoring ingress

## Prometheus-stack

helm upgrade --install -n monitoring prometheus-stack prometheus-community/kube-prometheus-stack -f kube-prometheus-stack.yaml

## INGRESS
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm upgrade --install nginx-ingress ingress-nginx/ingress-nginx --namespace ingress

## Cert-manager
helm upgrade --install cert-manager jetstack/cert-manager --namespace ingress --set installCRDs=true --set prometheus.enabled=true

<!-- 
## kubed 
helm repo add appscode https://charts.appscode.com/stable/  
helm upgrade --install kubed appscode/kubed --namespace kube-system -->
