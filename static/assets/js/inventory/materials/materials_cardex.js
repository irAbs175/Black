$(".do1").click(function() {
  let materialLocation = $("input[placeholder='material_location']").val();
  let materialHall = $(".MATERIAL_HALL").val();
  let materialCode = $("input[placeholder='material_code']").val();
  let materialColor = $("input[placeholder='material_color']").val();
  let factorNumber = $("input[placeholder='شماره حواله / فاکتور']").val();
  let factorRow = $("input[placeholder='ردیف فاکتور']").val();
  let number = $("input[placeholder='تعداد']").val();
  let description = $("input[placeholder='شرح اقدامات']").val();
  let operation = $("select:eq(0)").find(":selected").text();
  console.log(materialLocation);
  console.log(materialHall);
  console.log(materialCode);
  console.log(materialColor);
  let data = {
      'material_location' : materialLocation,
      'material_hall' : materialHall,
      'material_code' : materialCode,
      'material_color' : materialColor,
      'factor_number' : factorNumber,
      'factor_row' : factorRow,
      'number' : number,
      'description' : description,
      'operation' : operation,
  };
  $.ajax({
      url : '/inventory/js_update_materials',
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