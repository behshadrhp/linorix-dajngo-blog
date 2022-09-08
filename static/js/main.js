// Get search form and btn search
let search_form = document.getElementById('SearchForm');
let btn_page = document.getElementsByClassName('btn-page');

// Ensure search form exists 
if(search_form){
    for(let i=0; btn_page.length > i ; i++){
        btn_page[i].addEventListener('click', function(event) {
            event.preventDefault();
            
            // Get the data page
            let page = this.dataset.page;

            // Add Hidden search input to form 
            search_form.innerHTML += `<input value=${page} name='page' hidden />`;

            // Submit Form
            search_form.submit();
        })

    }
}