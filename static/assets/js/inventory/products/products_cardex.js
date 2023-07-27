$(".do1").click(function() {
  let productLocation = $("input[placeholder='product_location']").val();
  let productHall = $(".PRODUCT_HALL").val();
  let productCode = $("input[placeholder='product_code']").val();
  let productColor = $("input[placeholder='product_color']").val();
  let factorNumber = $("input[placeholder='شماره حواله / فاکتور']").val();
  let factorRow = $("input[placeholder='ردیف فاکتور']").val();
  let number = $("input[placeholder='تعداد']").val();
  let description = $("input[placeholder='شرح اقدامات']").val();
  let operation = $("select:eq(0)").find(":selected").text();
  let data = {
      'product_location' : productLocation,
      'product_hall' : productHall,
      'product_code' : productCode,
      'product_color' : productColor,
      'factor_number' : factorNumber,
      'factor_row' : factorRow,
      'number' : number,
      'description' : description,
      'operation' : operation,
  };
  $.ajax({
      url : '/inventory/js_update_products',
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
            location.reload(true)
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
});// End btn do1