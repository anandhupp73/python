january_customer={"c001","c002","c003","c004"}
february_customer={"c003","c004","c005","c006"}
march_customers={"c002","c004","c006","c007"}
print(january_customer.intersection(february_customer).intersection(march_customers))
print(january_customer.intersection(february_customer) | february_customer.intersection(march_customers) | january_customer.intersection(march_customers))