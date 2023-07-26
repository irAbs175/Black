$(".do1").click(function() {
  let productCode = $("input[name='CODE']").val();
  let factorNumber = $("input[placeholder='شماره حواله / فاکتور']").val();
  let number = $("input[placeholder='تعداد']").val();
  let description = $("input[placeholder='شرح اقدامات']").val();
  let operation = $("select:eq(0)").find(":selected").text();
  let data = {
      'product_code' : productCode,
      'factor_number' : factorNumber,
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