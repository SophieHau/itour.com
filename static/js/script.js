let numberControl = document.getElementById('id_number_of_people');
let tourControl = document.getElementById('id_tour');
let priceControl = document.getElementById('id_price');


tourControl.onchange = updatePrice;
numberControl.onchange = updatePrice;


function getPriceForSelectedTour() {
	let tourId = tourControl.value;
	console.log(TOUR_DATA)
	console.log(tourId)
	// look up price from tour ID
	let price = TOUR_DATA[tourId];
	return price;
}

function updatePrice() {
	let number = numberControl.value;
	let price = getPriceForSelectedTour();
	let total = number * price;
	priceControl.value = total;
}