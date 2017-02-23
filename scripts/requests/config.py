url = "http://127.0.0.1:7050/chaincode"

chaincode_id = "5036"

# Function name should be the first arg
deploy_args = ["init", "a", "100", "b", "200"]
invoke_args = ["transfer", "a", "b", "50"]
query_args = ["query", "a"]

