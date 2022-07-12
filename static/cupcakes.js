const BASE_URL = "http://127.0.0.1:5000"



$('.delete-cupcake').click(deleteCupcake)

async function deleteCupcake(evt){
    evt.preventDefault();
    const id = $(this).data('id')
    await axios.delete(`/api/cupcakes/${id}`)
    $(this).parent().remove()
}

