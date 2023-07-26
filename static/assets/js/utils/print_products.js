$(document).ready(function() {
function jPublish(date){
  let jDate = moment(date).format('jYYYY/jMM/jDD');
  let weekDay = moment(date).format('dddd');
  const weekDaysTranslation = {
    Monday: 'دوشنبه',
    Tuesday: 'سه‌شنبه',
    Wednesday: 'چهارشنبه',
    Thursday: 'پنجشنبه',
    Friday: 'جمعه',
    Saturday: 'شنبه',
    Sunday: 'یکشنبه',
  };
  let translatedWeekDay = weekDaysTranslation[weekDay];
  if (!translatedWeekDay) {
    translatedWeekDay = weekDay;
  }
  let jpubish = translatedWeekDay + ` ` +  jDate;
  return jpubish;
} // End function jPublish
  let product_name = $("input[name='PRODUCT_NAME']").val();
  let product_code = $("input[name='PRODUCT_CODE']").val();
  let product_color = $("input[name='PRODUCT_COLOR']").val();
  let product_location = $("input[name='PRODUCT_LOCATION']").val();
  let product_hall = $("input[name='PRODUCT_HALL']").val();
  let product_unit = $("input[name='PRODUCT_DATE']").val();
  let jpub = $("input[name='PRODUCT_UNIT']").val();
  
    $.get(`/inventory/api/products_cardex?search=${product_code}`, function (data) {
      let tableRows = '';
      for (let i = 0; i < data.count; i++) {
        let cardex = data.results[i];
        let dateTime = jPublish(cardex.date);
        let row = `
          <tr>
            <td>${cardex.row}</td>
            <td>${dateTime}</td>
            <td>${cardex.factor_number}</td>
            <td>${cardex.description}</td>
            <td>${cardex.status ? cardex.number : '0'}</td>
            <td>${cardex.status ? '0' : cardex.number}</td>
            <td>${cardex.quantity}</td>
            <td>${cardex.author}</td>
          </tr>
        `;
        tableRows += row;
      }
  
      let printContents = $('<div>').addClass('cardex').append(
        $('<div>').addClass('h-cardex').append(
          $('<span>').text(`نام کالا : ${product_name}`),
          $('<span>').text(`کد کالا : ${product_code}`),
          $('<span>').text(`رنگ کالا : ${product_color}`),
          $('<span>').text(`نام انبار : ${product_location}`),
          $('<span>').text(`محل کالا : ${product_hall}`),
          $('<span>').text(`واحد شمارش : ${product_unit}`),
          $('<span>').text(`تاریخ ثبت : ${jpub}`),
          $('<hr>'),
          $('<table>').addClass(`table`).append(
            $('<thead>').addClass(`table-dark`).append(
              $('<tr>').append(
                $('<th>').text(`ردیف`),
                $('<th>').text(`تاریخ`),
                $('<th>').text(`شماره فاکتور`),
                $('<th>').text(`شرح اقدامات`),
                $('<th>').text(`ورودی`),
                $('<th>').text(`خروجی`),
                $('<th>').text(`موجودی`),
                $('<th>').text(`اقدام کننده`),
              )
            ),
            $('<tbody>').append(tableRows)
          ),
        ),
      );
      $('.cardex').html(printContents);
    });
});//End Ready