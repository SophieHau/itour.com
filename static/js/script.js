let numberControl = document.getElementById('id_number_of_people');
let priceControl = document.getElementById('id_price')
const PRICE_PER_PERSON = priceControl.value;

numberControl.onchange = handleInput;

function handleInput() {
	let number = numberControl.value;
	let total = number * PRICE_PER_PERSON;
	priceControl.value = total;
}