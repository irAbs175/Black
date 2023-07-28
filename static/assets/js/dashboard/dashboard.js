function removeDuplicateProducts() {
    $('#PRODUCT .cardpro').each(function() {
      var $this = $(this);
      $this.siblings('.cardpro').filter(function() {
        return $(this).find('a').text() === $this.find('a').text();
      }).remove();
    });
  }// End function
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