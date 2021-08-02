provider "azurerm" { 
    features {}
    client_id = var.client_id
    subscription_id = var.subscription_id
    tenant_id = var.tenant_id
    client_secret = var.client_secret
}

variable "client_id" {}
variable "subscription_id" {}
variable "tenant_id" {}
variable "client_secret" {}
variable "location" {
    default = "southeastasia"
}
variable "dns_prefix" {
    default = "k8stest"
}
variable cluster_name {
    default = "k8stest"
}
variable resource_group_name {
    default = "azure-k8stest"
}