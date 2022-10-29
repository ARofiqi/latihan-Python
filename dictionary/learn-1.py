# pengenalan dictionary
data_dict = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3"
}

# mengambil data dict
data_1 = data_dict["key1"]

# mengambil data dengan perulangan for
[print(f"{i} = {data_dict[i]}") for i in data_dict]