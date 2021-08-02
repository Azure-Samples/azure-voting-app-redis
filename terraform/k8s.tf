resource "azurerm_resource_group" "k8s" {
    name = var.resource_group_name
    location = var.location
}

resource "azurerm_kubernetes_cluster" "k8s" {
    name = var.cluster_name
    location = azurerm_resource_group.k8s.location
    resource_group_name = azurerm_resource_group.k8s.name
    dns_prefix = var.dns_prefix

    default_node_pool {
        name = "agentpool"
        node_count =  1
        vm_size = "Standard_D2_v2"
    }

    service_principal {
        client_id =  var.client_id
        client_secret = var.client_secret
    }

    network_profile {
        load_balancer_sku = "Standard"
        network_plugin = "kubenet"
    }
}