## NS 
kubectl create namespace monitoring ingress

## Prometheus-stack

helm upgrade --install -n monitoring prometheus-stack prometheus-community/kube-prometheus-stack -f kube-prometheus-stack.yaml

## INGRESS
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm upgrade --install nginx-ingress ingress-nginx/ingress-nginx \
--namespace ingress \
--set controller.metrics.enabled=true \
--set-string controller.podAnnotations."prometheus\.io/scrape"="true" \
--set-string controller.podAnnotations."prometheus\.io/port"="10254"

## Cert-manager
helm upgrade --install cert-manager jetstack/cert-manager --namespace ingress --set installCRDs=true --set prometheus.enabled=true


## KEDA
helm repo add kedacore https://kedacore.github.io/charts
helm update --install keda kedacore/keda --namespace ingress-nginx

<!-- 
## kubed 
helm repo add appscode https://charts.appscode.com/stable/  
helm upgrade --install kubed appscode/kubed --namespace kube-system -->
