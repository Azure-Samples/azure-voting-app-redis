## NS 
kubectl create namespace monitoring ingress

## Prometheus
helm install prometheus --namespace monitoring --set alertmanager.enabled=false --set pushgateway.enabled=false --set server.persistentVolume.size=1000Gi --set server.persistentVolume.storageClass=azurefile-premium --set 'server.persistentVolume.accessModes={ReadWriteMany}' --set rbac.create=true stable/prometheus

kubectl -n monitoring expose deployment prometheus-server --name "prometheus-public"

## Grafana
helm install grafana grafana/grafana --namespace monitoring --set persistence.storageClassName=default --set persistence.enabled=true --set adminPassword=<pass> --set service.type=LoadBalancer

## INGRESS
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm install nginx-ingress ingress-nginx/ingress-nginx --namespace ingress