/*
function removeDuplicateProducts() {
    $('#PRODUCT .cardpro').each(function() {
      var $this = $(this);
      $this.siblings('.cardpro').filter(function() {
        return $(this).find('a').text() === $this.find('a').text();
      }).remove();
    });
  }
  
  $('.mSearch').click(function(event) {
    event.preventDefault();
    $('.searchResult').html("");
    $('.recentCardex').html("");
    var search_text = $('.rSearch').val();
  
    // Use Promise.all to ensure all API calls have finished before calling removeDuplicateProducts
    Promise.all([
      $.getJSON(`/inventory/api/products?search=${search_text}`),
      $.getJSON(`/inventory/api/materials?search=${search_text}`),
      $.getJSON(`/inventory/api/products_cardex?search=${search_text}`),
      $.getJSON(`/inventory/api/materials_cardex?search=${search_text}`)
    ]).then(function([productsData, materialsData, productsCardexData, materialsCardexData]) {
      if (productsData.count > 0) {
        for (let i = 0; i < productsData.count; i++) {
          let result = productsData.results[i];
          if (result.product_code == search_text) {
            let htmlResult = `
              <div class="mt-3">
                <div class="bkbc wttc itemkala">
                  <span>${result.product_name}</span>
                  <span>${result.product_code}</span>
                  <span>${result.product_color}</span>
                  <span>${result.product_quantity}</span>
                  <a href="/inventory/products/${result.product_code}"><span class="bi bi-pencil-fill"></span></a>
                </div>
              </div>
            `;
            $('.searchResult').append(htmlResult);
          }
        }
      }
  
      if (materialsData.count > 0) {
        for (let i = 0; i < materialsData.count; i++) {
          let result = materialsData.results[i];
          if (result.material_code == search_text) {
            let htmlResult = `
              <div class="mt-3">
                <div class="bkbc wttc itemkala">
                  <span>${result.material_name}</span>
                  <span>${result.material_code}</span>
                  <span>${result.material_color}</span>
                  <span>${result.material_quantity}</span>
                  <a href="/inventory/materials/${result.material_code}"><span class="bi bi-pencil-fill"></span></a>
                </div>
              </div>
            `;
            $('.searchResult').append(htmlResult);
          }
        }
      }
  
      if (productsCardexData.count > 0) {
        for (let i = 0; i < productsCardexData.count; i++) {
          let result = productsCardexData.results[i];
          if (result.product == search_text) {
            let htmlResult = `
              <div class="mt-3">
                <div class="bkbc wttc itemkala">
                  <span>${result.product}</span>
                  <span>${result.factor_number}</span>
                  <span>${result.description}</span>
                  <span>${result.operation}</span>
                  <span>${result.number}</span>
                  <a href="/inventory/products/${result.product}"><span class="bi bi-pencil-fill"></span></a>
                </div>
              </div>
            `;
            $('.searchResult').append(htmlResult);
          }
        }
      }
  
      if (materialsCardexData.count > 0) {
        for (let i = 0; i < materialsCardexData.count; i++) {
          let result = materialsCardexData.results[i];
          if (result.material == search_text) {
            let htmlResult = `
              <div class="mt-3">
                <div class="bkbc wttc itemkala">
                  <span>${result.material}</span>
                  <span>${result.factor_number}</span>
                  <span>${result.description}</span>
                  <span>${result.operation}</span>
                  <span>${result.number}</span>
                  <a href="/inventory/materials/${result.material}"><span class="bi bi-pencil-fill"></span></a>
                </div>
              </div>
            `;
            $('.searchResult').append(htmlResult);
          }
        }
      }
  
      // Call removeDuplicateProducts after all API calls have finished
      removeDuplicateProducts();
    }).catch(function(error) {
      console.error(error);
      // Add error handling here
    });
  });
*/
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
    $('.searchResult').html("");
    $('.recentCardex').html("");
    var search_text = $('.rSearch').val();
    $.getJSON(`/inventory/api/products?search=${search_text}`, function(data) {
        if(data.count > 0){
            for(let i = 0; i < data.count; i++){
                let result = data.results[i];
                if(result.product_code === search_text){
                    let htmlResult = `
                    <div class="mt-3">
                <div class="bkbc wttc itemkala">
                    <span>${result.product_name}</span>
                    <span>${result.product_code}</span>
                    <span>${result.product_color}</span>
                    <span>${result.product_quantity}</span>
                    <a href="/inventory/products/${result.product_code}"><span class="bi bi-pencil-fill"></span></a>
    
                </div>
            </div>
                    `;
                    $('.searchResult').append(htmlResult);
                };// End if
            };//End for
            removeDuplicateProducts();
        };// End if
        return;
    }); //End getJSON Products
    $.getJSON(`/inventory/api/materials?search=${search_text}`, function(data) {
        if(data.count > 0){
            for(let i = 0; i < data.count; i++){
                let result = data.results[i];
                if(result.material_code === search_text){
                    let htmlResult = `
                    <div class="mt-3">
                <div class="bkbc wttc itemkala">
                    <span>${result.material_name}</span>
                    <span>${result.material_code}</span>
                    <span>${result.material_color}</span>
                    <span>${result.material_quantity}</span>
                    <a href="/inventory/materials/${result.material_code}"><span class="bi bi-pencil-fill"></span></a>
    
                </div>
            </div>
                    `;
                    $('.searchResult').append(htmlResult);
                }; // End if
            };//End for
            removeDuplicateProducts();
        };// End if
    }); //End getJSON Materials
    $.getJSON(`/inventory/api/products_cardex?search=${search_text}`, function(data) {
        if(data.count > 0){
            for(let i = 0; i < data.count; i++){
                let result = data.results[i];
                if(result.product === search_text){
                    let htmlResult = `
                    <div class="mt-3">
                <div class="bkbc wttc itemkala">
                    <span>${result.product}</span>
                    <span>${result.factor_number}</span>
                    <span>${result.description}</span>
                    <span>${result.operation}</span>
                    <span>${result.number}</span>
                    <a href="/inventory/products/${result.product}"><span class="bi bi-pencil-fill"></span></a>
                </div>
            </div>
                    `;
                    $('.csearchResult').append(htmlResult);
                }; // End if
            };//End for
            removeDuplicateProducts();
        };// End if
    }); //End getJSON ProductsCardex
    $.getJSON(`/inventory/api/materials_cardex?search=${search_text}`, function(data) {
        if(data.count > 0){
            for(let i = 0; i < data.count; i++){
                let result = data.results[i];
                if(result.material === search_text){
                    let htmlResult = `
                    <div class="mt-3">
                <div class="bkbc wttc itemkala">
                    <span>${result.material}</span>
                    <span>${result.factor_number}</span>
                    <span>${result.description}</span>
                    <span>${result.operation}</span>
                    <span>${result.number}</span>
                    <a href="/inventory/materials/${result.material}"><span class="bi bi-pencil-fill"></span></a>
                </div>
            </div>
                    `;
                    $('.searchResult').append(htmlResult);
                }; // End if
            };//End for
            removeDuplicateProducts();
        };// End if
    }); //End getJSON MaterialsCardex
});// End .mSearch click 