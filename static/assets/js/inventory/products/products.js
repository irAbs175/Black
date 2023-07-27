function edit_product(location, hall, code, color){
    window.location.href = `/inventory/products/${location}^${code}^${color}`;
}// End function edit_product