$(document).ready(function() {
    console.log('+> Hi!');
});// End ready
$(".do0").click(function() {
    let productName = $(".productName").val();
    let productCode = $(".productCode").val();
    let productColor = $(".productColor").val();
    let productLocation = $("select:eq(0)").find(":selected").text();
    let productHall = $("select:eq(1)").find(":selected").text();
    let productUnit = $("select:eq(2)").find(":selected").text();
    let data = {
        'product_name' : productName,
        'product_code' : productCode,
        'product_color' : productColor,
        'product_location' : productLocation,
        'product_hall' : productHall,
        'product_unit' : productUnit,
    };
    $.ajax({
        url : '/inventory/js_add_products',
        type : 'POST',
        data : data,
        success: function(response) {
            if (response.success === false) {
              Swal.fire({
                icon: "error",
                title: response.status,
                showConfirmButton: false,
                timer: 3000,
              });
            } else {
              Swal.fire({
                icon: "success",
                title: response.status,
                showConfirmButton: false,
                timer: 2000,
              });
              window.location.href = `/inventory/products/${product_location}/${productHall}/${productCode}/${productColor}`;
            }
          },
          error: function(xhr, status, error) {
            console.log(status);
            Swal.fire({
              icon: "error",
              title: status,
              showConfirmButton: false,
              timer: 3000,
            });
          }
    });//End ajax
});// End btn do0