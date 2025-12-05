def test_product_details():
    expected_output = (
        "Product Name: Mobile\n"
        "Product ID: E1001\n"
        "Quantity: 10\n"
        "Price: 15000"
    )

    assert product_details("Mobile", "E1001", 10, 15000) == expected_output
