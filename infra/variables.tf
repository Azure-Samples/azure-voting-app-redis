variable "subscription_id" {
  description = "fb78e43e-3e05-43c2-91aa-fdecd649ae2c"
  type        = string
}

variable "resource_group_name" {
  type    = string
  default = "rg-aks-devops"
}

variable "location" {
  type    = string
  default = "germanywestcentral"
}

variable "acr_name" {
  description = "acrelazzouzidevops"
  type        = string
}

variable "aks_name" {
  type    = string
  default = "aks-devops-demo"
}


