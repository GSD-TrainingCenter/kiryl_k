function myFunction() {
	let input, filter, ul, li, a, i;
	input = document.getElementById('search-box');
	filter = input.value.toUpperCase();
	ul = document.getElementById('myUL');
	a = ul.getElementsByTagName('a');
		for (i = 0; i < a.length; i++) {
		li = a[i].getElementsByTagName('li')[0];
		if (li.innerHTML.toUpperCase().indexOf(filter) > -1) {
			a[i].style.display = "";
		} else {
			a[i].style.display = "none";
		}
	}
}