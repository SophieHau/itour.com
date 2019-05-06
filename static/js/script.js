let numberControl = document.getElementById('id_number_of_people');
let tourControl = document.getElementById('id_tour');
let priceControl = document.getElementById('id_price');

tourControl.onchange = manageChangeID;
numberControl.onchange = updatePrice;


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

           review = data['rating'] + ' by ' + data['user'] + ' in ' + data['date']
           // $( '#message' ).text(review);
           $('#message').html('<i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i><i class="fa fa-star text-success"></i>' + ' by ' + data['user'] + ' in ' + data['date'])
          }
        });

   }