const filter =  document.querySelector('#filter')


if(filter){
    filter.addEventListener('change', e => {
        document.querySelector('#filter').submit()
    })
}