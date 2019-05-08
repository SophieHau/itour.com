let numberControl = document.getElementById('id_number_of_people');
let tourControl = document.getElementById('id_tour');
let priceControl = document.getElementById('id_price');

tourControl.onchange = manageChangeID;
numberControl.onchange = updatePrice;
window.onload = showReviews;

function getPriceForSelectedTour() {
	let tourId = tourControl.value;
	console.log(TOUR_DATA)
	console.log(tourId)
	// look up price from tour ID
	let price = TOUR_DATA[tourId];
	return price;
}

function manageChangeID() {
	updatePrice();
	showReviews();
}

function updatePrice() {
	let number = numberControl.value;
	let price = getPriceForSelectedTour();
	let total = number * price;
	priceControl.value = total;

}

function formatDate(date) {
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? 'pm' : 'am';
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? '0'+minutes : minutes;
  var strTime = hours + ':' + minutes + ' ' + ampm;
  return date.getMonth()+1 + "/" + date.getDate() + "/" + date.getFullYear() + "  " + strTime;
}

function showReviews() {
	let tourId = tourControl.value;

	console.log('antes ');

	  $.ajax({
        url: '/fetch_reviews/'+tourId,
        data: {
          'tour_id': tourId
        },
        dataType: 'json',
        success: function (data) { 
        	// console.log(data[tour_id]);	
        	console.log(data);
        	console.log(tourId);
        	// console.log(data['json'][0])
           // $( '#message' ).text(data['json'][0]['user_id']);

           // review = data['rating'] + ' by ' + data['user'] + ' in ' + 
			// print('review')
			// print(data['rating'])
			excelent = '<i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i>';
			verygood = '<i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i><small><i class="fa fa-star text-muted bg-transparent"></i></small>';
			good = '<i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i><small><i class="fa fa-star text-muted bg-transparent"></i><i class="fa fa-star text-muted bg-transparent"></i></small>';
			fair = '<i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i><i class="fa fa-star text-success"><small></i><i class="fa fa-star text-muted bg-transparent"></i><i class="fa fa-star text-muted bg-transparent"></i><i class="fa fa-star text-muted bg-transparent"></i></small>';
			poor = '<i class="fa fa-star text-success"></i><small><i class="fa fa-star text-muted bg-transparent"></i><i class="fa fa-star text-muted bg-transparent"></i><i class="fa fa-star text-muted bg-transparent"></i><i class="fa fa-star text-muted bg-transparent"></i></small>';
			if (data['rating'] === 'excelent') {
				stars = excelent;
			}
			else if (data['rating'] === 'very good') {
				stars = verygood;
			}
			else if (data['rating'] === 'good') {
				stars = good;
			}
			else if (data['rating'] === 'fair') {
				stars = fair;
			}
			else if (data['rating'] === 'poor') {
				stars = poor;
			}
			date_review = Date(data['date']);	
			// let formatted_date = date_review + "-" + (date_review.getMonth() + 1) + "-" + date_review.getFullYear();
			$('#message').html(stars + ' by ' + data['user'] + ' in ' + '<small>' + date_review + '</small>');
          	}
			});
	}