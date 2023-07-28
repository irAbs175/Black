function edit_product(location, hall, code, color){
    window.location.href = `/inventory/products/${location}^${code}^${color}`;
}// End function edit_product
$('.mSearch').click(function(event) {
    event.preventDefault();
    var search_text = $('.rSearch').val();
    if(search_text != ''){
      window.location.href = `/search/${search_text}`;
    }else{
      Swal.fire({
        icon: "error",
        title: 'جستجو خالی است‌!',
        showConfirmButton: false,
        timer: 3000,
      });
    };
});