from woocommerce import API

wcapi = API(
    url="https://ip22.asot.uz/",
    consumer_key="ck_7985e5deb4a0f8c3e26d413404a39bab90776126",
    consumer_secret="cs_19a2286226326c905c2d53ba881bff6c655c3233",
    version="wc/v3"
)

print(wcapi.get("products", params={"per_page": 20}).json())
