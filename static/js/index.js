var list_data = {};


$(document).ready(function () {

  $('select').formSelect();

});

$('#todayCases').animateNumber(
  {
    number: parseInt($('#todayCases').text()),
    color: 'red',
    font-size: '30px',
	width: '100%'
	
  },
  {
    easing: 'swing',
    duration: 15000
  }
);
$('#todayDeaths').animateNumber(
    {
      number: parseInt($('#todayDeaths').text()),
      color: 'red',
      font-size: '30px'
    },
    {
      easing: 'swing',
      duration: 15000
    }
  );
  $('#totalCases').animateNumber(
    {
      number: parseInt($('#totalCases').text()),
      color: 'red',
      font-size: '30px'
    },
    {
      easing: 'swing',
      duration: 15000
    }
  );
  $('#totalDeaths').animateNumber(
    {
      number: parseInt($('#totalDeaths').text()),
      color: 'red',
      font-size: '30px'
    },
    {
      easing: 'swing',
      duration: 15000
    }
  );
   $('#totalRecovery').animateNumber(
    {
      number: parseInt($('#totalRecovery').text()),
      color: 'red',
      font-size: '30px'
    },
    {
      easing: 'swing',
      duration: 15000
    }
  );

