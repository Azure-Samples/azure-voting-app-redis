if [ $(az group exists --name $RESOURCEGROUPNAME) = false ]; 
then
    cd aks_cluster
    terraform init $tf_init_cli_options
    terraform apply -var "client_id=$client_id" -var "subscription_id=$subscription_id" -var "tenant_id=$tenant_id" -var "client_secret=$client_secret" $tf_apply_cli_options
    cd ../
else
    echo resource group exist
    exit 0
fi